from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# TDOD: implement lazy Caching because we don't want to keep everything in memory
# TODO: Implement pagination to limit memory usage
# TODO: Implement parent/child datasources so that we can specify them in code

class DataSource:
    def __init__(self, metadata, table_name):
        self.engine = metadata.bind
        self.table = metadata.tables[table_name]
        self.Session = sessionmaker(bind=self.engine)
        self.listeners = []
        self._current_row_index = 0
        self._current_column_index = 0
        self._data_cache = self.get_data()

    @property
    def column_names(self):
        return [column.name for column in self.table.columns]

    @property
    def current_row(self):
        if self._data_cache:
            return self._data_cache[self._current_row_index]
        return None

    @property
    def current_column(self):
        if self.current_row:
            column_name = self.column_names[self._current_column_index]
            return self.current_row[column_name]
        return None

    @property
    def row_count(self):
        return len(self._data_cache)

    @property
    def current_row_index(self):
        return self._current_row_index

    @current_row_index.setter
    def current_row_index(self, index):
        if 0 <= index < self.row_count:
            self._current_row_index = index
            self.notify_listeners()

    @property
    def current_column_index(self):
        return self._current_column_index

    @current_column_index.setter
    def current_column_index(self, index):
        if 0 <= index < len(self.column_names):
            self._current_column_index = index
            self.notify_listeners()

    # ... (rest of the methods remain the same)

    def notify_listeners(self):
        # Notify listeners of the change
        for listener in self.listeners:
            listener.on_data_changed(self.current_row)

    def add_listener(self, listener):
        self.listeners.append(listener)

    def remove_listener(self, listener):
        self.listeners.remove(listener)

    def notify_listeners(self):
        for listener in self.listeners:
            listener.on_data_changed(self.get_data())

    def get_data(self):
        session = self.Session()
        data = session.query(self.table).all()
        session.close()
        return data

    def get_record(self, record_id):
        session = self.Session()
        record = session.query(self.table).get(record_id)
        session.close()
        return record

    def update_record(self, record_id, new_data):
        session = self.Session()
        record = session.query(self.table).get(record_id)
        if record:
            for key, value in new_data.items():
                setattr(record, key, value)
            session.commit()
        session.close()
        self.notify_listeners()

    def delete_record(self, record_id):
        session = self.Session()
        record = session.query(self.table).get(record_id)
        if record:
            session.delete(record)
            session.commit()
        session.close()
        self.notify_listeners()

class UIComponent:
    def on_data_changed(self, data):
        # Update the UI component with new data
        pass

# Example usage
db_url = 'sqlite:///your_database.db'  # Replace with your database URL
table_name = 'your_table_name'         # Replace with your table name
data_source = DataSource(db_url, table_name)
ui_component = UIComponent()
data_source.add_listener(ui_component)
