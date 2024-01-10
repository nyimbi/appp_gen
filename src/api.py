from flask_appbuilder.api import BaseApi, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from .models import *

class Agent_tierRestApi(BaseApi):
    resource_name = "agent_tier"
    datamodel = SQLAInterface(Agent_tier)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Agent_tierRestApi)

class BankRestApi(BaseApi):
    resource_name = "bank"
    datamodel = SQLAInterface(Bank)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(BankRestApi)

class Biller_categoryRestApi(BaseApi):
    resource_name = "biller_category"
    datamodel = SQLAInterface(Biller_category)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Biller_categoryRestApi)

class CountryRestApi(BaseApi):
    resource_name = "country"
    datamodel = SQLAInterface(Country)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(CountryRestApi)

class CouponRestApi(BaseApi):
    resource_name = "coupon"
    datamodel = SQLAInterface(Coupon)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(CouponRestApi)

class Customer_segmentRestApi(BaseApi):
    resource_name = "customer_segment"
    datamodel = SQLAInterface(Customer_segment)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Customer_segmentRestApi)

class Doc_typeRestApi(BaseApi):
    resource_name = "doc_type"
    datamodel = SQLAInterface(Doc_type)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Doc_typeRestApi)

class Payment_cardRestApi(BaseApi):
    resource_name = "payment_card"
    datamodel = SQLAInterface(Payment_card)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Payment_cardRestApi)

class PromotionRestApi(BaseApi):
    resource_name = "promotion"
    datamodel = SQLAInterface(Promotion)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(PromotionRestApi)

class Token_providerRestApi(BaseApi):
    resource_name = "token_provider"
    datamodel = SQLAInterface(Token_provider)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Token_providerRestApi)

class Trans_routing_thresholdsRestApi(BaseApi):
    resource_name = "trans_routing_thresholds"
    datamodel = SQLAInterface(Trans_routing_thresholds)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Trans_routing_thresholdsRestApi)

class Trans_typeRestApi(BaseApi):
    resource_name = "trans_type"
    datamodel = SQLAInterface(Trans_type)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Trans_typeRestApi)

class User_extRestApi(BaseApi):
    resource_name = "user_ext"
    datamodel = SQLAInterface(User_ext)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(User_extRestApi)

class BillerRestApi(BaseApi):
    resource_name = "biller"
    datamodel = SQLAInterface(Biller)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(BillerRestApi)

class DocRestApi(BaseApi):
    resource_name = "doc"
    datamodel = SQLAInterface(Doc)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(DocRestApi)

class StateRestApi(BaseApi):
    resource_name = "state"
    datamodel = SQLAInterface(State)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(StateRestApi)

class Token_listsRestApi(BaseApi):
    resource_name = "token_lists"
    datamodel = SQLAInterface(Token_lists)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Token_listsRestApi)

class Biller_offeringRestApi(BaseApi):
    resource_name = "biller_offering"
    datamodel = SQLAInterface(Biller_offering)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Biller_offeringRestApi)

class LgaRestApi(BaseApi):
    resource_name = "lga"
    datamodel = SQLAInterface(Lga)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(LgaRestApi)

class AgentRestApi(BaseApi):
    resource_name = "agent"
    datamodel = SQLAInterface(Agent)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(AgentRestApi)

class PosRestApi(BaseApi):
    resource_name = "pos"
    datamodel = SQLAInterface(Pos)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(PosRestApi)

class Agent_doc_linkRestApi(BaseApi):
    resource_name = "agent_doc_link"
    datamodel = SQLAInterface(Agent_doc_link)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Agent_doc_linkRestApi)

class Comm_refRestApi(BaseApi):
    resource_name = "comm_ref"
    datamodel = SQLAInterface(Comm_ref)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Comm_refRestApi)

class PersonRestApi(BaseApi):
    resource_name = "person"
    datamodel = SQLAInterface(Person)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(PersonRestApi)

class Pos_agent_linkRestApi(BaseApi):
    resource_name = "pos_agent_link"
    datamodel = SQLAInterface(Pos_agent_link)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Pos_agent_linkRestApi)

class WalletRestApi(BaseApi):
    resource_name = "wallet"
    datamodel = SQLAInterface(Wallet)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(WalletRestApi)

class Agent_personRestApi(BaseApi):
    resource_name = "agent_person"
    datamodel = SQLAInterface(Agent_person)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Agent_personRestApi)

class Person_doc_linkRestApi(BaseApi):
    resource_name = "person_doc_link"
    datamodel = SQLAInterface(Person_doc_link)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(Person_doc_linkRestApi)

class TransRestApi(BaseApi):
    resource_name = "trans"
    datamodel = SQLAInterface(Trans)

    @expose("/", methods=["GET"])
    def get_list(self):
        """Get list of records."""
        return self.list()

    @expose("/<pk>", methods=["GET"])
    def get_item(self, pk):
        """Get record by primary key."""
        return self.show(pk)

    @expose("/", methods=["POST"])
    def post(self):
        """Create a new record."""
        return self.post()

    @expose("/<pk>", methods=["PUT"])
    def put(self, pk):
        """Update existing record."""
        return self.edit(pk)

    @expose("/<pk>", methods=["DELETE"])
    def delete(self, pk):
        """Delete record by primary key."""
        return self.delete(pk)

appbuilder.add_api(TransRestApi)

