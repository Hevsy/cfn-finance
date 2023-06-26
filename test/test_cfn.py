import pytest
from pathlib import Path
from cloud_radar.cf.unit import Template


@pytest.fixture
def template():
    template_path = Path(__file__).parent / "../finance1.yaml"
    return Template.from_yaml(template_path.resolve())


@pytest.fixture
def params():
    return {"KeyName": "your-key-name"}


@pytest.mark.parametrize(
    "resource_name",
    [
        "FinanceVPC",
        "FinanceWebServer",
        "PrivateSubnet1",
        "PrivateSubnet2",
        "PrivateSubnet3",
        "PrivateSubnet4",
        "PublicSubnet1",
        "PublicSubnet2",
        "FinanceIGW",
        "AttachGateway",
        "PublicRT",
        "PublicRT1Association",
        "PublicRT2Association",
        "PrivateRT1Association",
        "PrivateRT2Association",
    ],
)
def test_network_resources(template, params, resource_name):
    stack = template.render(params)
    assert resource_name in stack["Resources"]


@pytest.mark.parametrize(
    "resource_name",
    [
        "WebSG", 
        "SSHSG", 
        "EC2toRDSSG", 
        "EC2toRDSegress", 
        "RDStoEC2SG", 
        "RDStoEC2ingress"],
)
def test_security_groups(template, params, resource_name):
    stack = template.render(params)
    assert resource_name in stack["Resources"]


@pytest.mark.parametrize(
        "resource_name", 
        [
            "DBSubnetGroup1", 
            "FinanceDB"
            ]
            )
def test_database_resources(template, params, resource_name):
    stack = template.render(params)
    assert resource_name in stack["Resources"]


@pytest.mark.parametrize(
        "resource_name", 
        [
            "FinanceALB", 
            "FinanceTargetGroup"
            ]
            )
def test_load_balancer_resources(template, params, resource_name):
    stack = template.render(params)
    assert resource_name in stack["Resources"]


@pytest.mark.parametrize("resource_name", ["FinanceASG", "FinanceLaunchConfiguration"])
def test_auto_scaling_resources(template, params, resource_name):
    stack = template.render(params)
    assert resource_name in stack["Resources"]
