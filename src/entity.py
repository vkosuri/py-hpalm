
"""
Description
    The meta-data for an entitity type defined in the project. 
URL
    http://host:port/qcbin/rest/domains/{domain}/projects/{project}/{Entity Name}/{Entity Property}
HTTP Methods
    GET: Retrieves the collection entity types.
    PUT: Updates
    DELETE: Deletes
    POST: Varieis
"""
from lxml import etree
from hpalm import ALMException
from hpalm import HPALM
import logging
import os

logger = logging.getLogger(__name__)

def text_xml(xml, xpath):
    dom_tree = etree.fromstring(xml)
    return dom_tree.xpath(xpath)

class TestLab(HPALM):
    def __init__(self):
        super(self.__class__, self).__init__()

    def get_testset_inst(self, tid):
        """
        This procedure will return list of test-instances in a given test set
        :param hp: HP object
        :param tid: integer test set identifier
        :returns: list test instances list
        """
        domain = self.domain
        project = self.project
        params = '{cycle-id[' + tid + ']}'
        url = self.base_url + '/qcbin/rest/domains/' + domain + '/projects/' + project + '/test-instances'
        response = self.s.get(url, params=params, headers=self.getheaders())
        test_inst = text_xml(response.content, "Entity/Fields/Field\[@Name='test-instance'\]/Value/text()")
        return test_inst

class Tests(object):
    """
    The Test with the specified ID. 
    URL
        http://host:port/qcbin/rest/domains/{domain}/projects/{Project ID}/tests/{Test ID} 
    HTTP Methods
        GET: Returns the Test.
        PUT: Updates the Test.
        DELETE:Deletes the Test.
        POST: N/A
    """
    def __init__(self):
        pass

class defects(object):
    def __init__(self):
        pass
        
class TestSet(TestLab):
    def __init__(self):
        super(self.__class__, self).__init__()

    def create(self,path):
        pass
    def delete(self, path):
        pass

class TestInstance(TestSet):
    def __init__(self):
        super(self.__class__, self).__init__()

    def create(self, path):
        pass

    def delete(self, path):
        pass

    def get_test_instance_run_id(self, domain, project, testset_id, test_id, test_ins):
        pass

class Runs(TestInstance):
    def __init__(self):
        super(self.__class__, self).__init__()

    def create(self, path):
        pass

    def delete(self, path):
        pass

    def attach_file(self, id, full_path):
        """
        Attach file to test instance run
        """
        fd = None
        ftext = None
        if os.path.getsize(full_path) > 0:
            fd = open(full_path, "r")
            ftext = fd.read()
        else:
            raise ALMException("Unable to find file")
        # get filename    
        fname = os.path.basename(full_path)
        headers = self.getheaders()
        headers['content-type'] = 'application/octet-stream'
        headers['slug'] = fname
        uri = self.base_url + self.uri
        resp = self.s.post(uri, params=ftext, headers=headers)
        if resp.status_code == 201:
            logger.info("Sucessfully attached file: %s size: %d" %(fname, len(ftext)))
        else:
            logger.error("Failed to create to attachement file: %s size: %d" %(fname, len(ftext)))
        return resp.status_code
    
    def get_attached_file(self, uri):
        headers = self.getheaders()
        uri = self.base_url + uri
        headers['Accept'] = 'application/octet-stream'
        resp = self.s.get(uri, headers=headers)
        if resp.status_code == 200:
            logger.info("%s data read from file" %(resp.text))
        