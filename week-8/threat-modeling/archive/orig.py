#!/usr/bin/env python3

from pytm.pytm import TM, Server, Datastore, Dataflow, Boundary, Actor, Lambda, ExternalEntity

tm = TM("Praxis")
tm.description = "Application of Reinforcement Learning Methodology to Improve Robustness of Data Breach Controls"
tm.isOrdered = True

datacenter = Boundary("Class-3 Datacenter")
aws = Boundary("AWS")
anywhere = Boundary("Anywhere")
saas_zone = Boundary("SaaS Zone")
trust_zone = Boundary("Trust Zone")

trust_zone.inBoundary = aws

employees = Actor("BW Users")
client = Actor("BW Clients")
cs_tech_ops = Actor("CS Tech Ops")
cs_client_team = Actor("Client Team")

employees.inBoundary = anywhere
client.inBoundary = anywhere
cs_client_team.inBoundary = anywhere
cs_tech_ops.inBoundary = datacenter

jumpstation = Server("Class-3 Jumpstation")
jumpstation.inBoundary = datacenter
jumpstation.OS = "Windows"
jumpstation.isHardened = True

iam_gw = Server("IAM Gateway")
iam_gw.inBoundary = aws
# iam_gw.isHardened = True

okta_saas = ExternalEntity("Okta SaaS")
okta_saas.inBoundary = saas_zone

view = Server("BCO Web")
view.inBoundary = trust_zone

controller = Server("GraphQL Engine")
controller.inBoundary = trust_zone

model = Datastore("CMS")
model.inBoundary = trust_zone

client_db = Datastore("Client Accounts DB")
client_db.inBoundary = aws
client_db.inScope = True
client_db.storesPII = True

salesforce_saas = ExternalEntity("Salesforce SaaS")
salesforce_saas.inBoundary = saas_zone

bw_azure_ad = ExternalEntity("Azure AD SaaS")
bw_azure_ad.inBoundary = saas_zone

client_to_iam_gw_1 = Dataflow(client, iam_gw, "BCO login")
client_to_iam_gw_1.protocol = "HTTPS"
client_to_iam_gw_1.dstPort = 443

iam_gw_to_client_1 = Dataflow(iam_gw, client, "Redirect to authorize")
iam_gw_to_client_1.protocol = "HTTPS"
iam_gw_to_client_1.dstPort = 443

client_to_okta_saas_1 = Dataflow(client, okta_saas, "Authorize user")
client_to_okta_saas_1.protocol = "HTTPS"
client_to_okta_saas_1.dstPort = 443

okta_saas_to_client_1 = Dataflow(okta_saas, client, "Issue authorization token")
okta_saas_to_client_1.protocol = "HTTPS"
okta_saas_to_client_1.dstPort = 443

client_to_iam_gw_2 = Dataflow(client, iam_gw, "BCO login with token")
client_to_iam_gw_2.protocol = "HTTPS"
client_to_iam_gw_2.dstPort = 443

iam_gw_to_view = Dataflow(iam_gw, view, "Allow BCO connection")
iam_gw_to_view.protocol = "HTTPS"
iam_gw_to_view.dstPort = 443

view_to_controller = Dataflow(view, controller, "Query content")
view_to_controller.protocol = "HTTPS"
view_to_controller.dstPort = 443

controller_to_model = Dataflow(controller, model, "Access content")
controller_to_model.protocol = "HTTPS"
controller_to_model.dstPort = 443

model_to_controller = Dataflow(model, controller, "Return content")
model_to_controller.protocol = "HTTPS"
model_to_controller.dstPort = 443

controller_to_view = Dataflow(controller, view, "Render content")
controller_to_view.protocol = "HTTPS"
controller_to_view.dstPort = 443

view_to_iam_gw = Dataflow(view, iam_gw, "Pass through connection")
view_to_iam_gw.protocol = "HTTPS"
view_to_iam_gw.dstPort = 443

iam_gw_to_client_2 = Dataflow(iam_gw, client, "Present content")
iam_gw_to_client_2.protocol = "HTTPS"
iam_gw_to_client_2.dstPort = 443


cs_client_team_to_salesforce_saas = Dataflow(cs_client_team, salesforce_saas, "Onboard new client")
cs_client_team_to_salesforce_saas.protocol = "HTTPS"
cs_client_team_to_salesforce_saas.dstPort = 443

salesforce_saas_to_client_db = Dataflow(salesforce_saas, client_db, "Update client DB")
salesforce_saas_to_client_db.protocol = "HTTPS"
salesforce_saas_to_client_db.dstPort = 443

client_db_to_okta_saas = Dataflow(client_db, okta_saas, "Update Okta records")
client_db_to_okta_saas.protocol = "HTTPS"
client_db_to_okta_saas.dstPort = 443

okta_saas_to_client_db = Dataflow(okta_saas, client_db, "Confirm Okta updates")
okta_saas_to_client_db.protocol = "HTTPS"
okta_saas_to_client_db.dstPort = 443

client_db_to_salesforce_saas = Dataflow(client_db, salesforce_saas, "Update Salesforce records")
client_db_to_salesforce_saas.protocol = "HTTPS"
client_db_to_salesforce_saas.dstPort = 443

salesforce_saas_to_cs_client_team = Dataflow(salesforce_saas, cs_client_team, "Acknowledge new client")
salesforce_saas_to_cs_client_team.protocol = "HTTPS"
salesforce_saas_to_cs_client_team.dstPort = 443

employees_to_iam_gw = Dataflow(employees, iam_gw, "BCO login via SSO")
employees_to_iam_gw.protocol = "HTTPS"
employees_to_iam_gw.dstPort = 443

iam_gw_to_okta_saas_11 = Dataflow(iam_gw, okta_saas, "Verify access")
iam_gw_to_okta_saas_11.protocol = "HTTPS"
iam_gw_to_okta_saas_11.dstPort = 443

okta_saas_to_bw_azure_ad_12 = Dataflow(okta_saas, bw_azure_ad, "Request SAML token")
okta_saas_to_bw_azure_ad_12.protocol = "HTTPS"
okta_saas_to_bw_azure_ad_12.dstPort = 443

bw_azure_ad_to_okta_saas_13 = Dataflow(bw_azure_ad, okta_saas, "Issue SAML token")
bw_azure_ad_to_okta_saas_13.protocol = "HTTPS"
bw_azure_ad_to_okta_saas_13.dstPort = 443

okta_saas_to_iam_gw_14 = Dataflow(okta_saas, iam_gw, "Confirm identify")
okta_saas_to_iam_gw_14.protocol = "HTTPS"
okta_saas_to_iam_gw_14.dstPort = 443

iam_gw_to_view_15 = Dataflow(iam_gw, view, "Allow BCO access")
iam_gw_to_view_15.protocol = "HTTPS"
iam_gw_to_view_15.dstPort = 443

view_to_iam_gw_16 = Dataflow(view, iam_gw, "Pass through content")
view_to_iam_gw_16.protocol = "HTTPS"
view_to_iam_gw_16.dstPort = 443

iam_gw_to_employees_17 = Dataflow(iam_gw, employees, "Present content")
iam_gw_to_employees_17.protocol = "HTTPS"
iam_gw_to_employees_17.dstPort = 443

cs_tech_ops_to_datacenter = Dataflow(cs_tech_ops, jumpstation, "Dual key operations")
cs_tech_ops_to_datacenter.protocol = "RDP"
cs_tech_ops_to_datacenter.dstPort = 3389

jumpstation_to_aws = Dataflow(jumpstation, iam_gw, "AWS operations")
jumpstation_to_aws.protocol = "SSH"
jumpstation_to_aws.dstPort = 22
# jumpstation_to_okta_saas = Dataflow(jumpstation, okta_saas, "Okta operations")
# jumpstation_to_view = Dataflow(jumpstation, view, "BCO operations")
# jumpstation_to_controller = Dataflow(jumpstation, controller, "Controller operations")
# jumpstation_to_model = Dataflow(jumpstation, model, "CMS operations")
# jumpstation_to_client_db = Dataflow(jumpstation, client_db, "Client DB operations")

tm.process()