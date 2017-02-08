
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
from hpalm import ALMMethodNotImplementedException
from hpalm import HPALM
from hpalm import text_to_xml
import logging
import os
import requests

logger = logging.getLogger(__name__)

class TestLab(HPALM):
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

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
        response = requests.get(url, params=params, headers=self.getheaders())
        test_inst = text_to_xml(response.content, "Entity/Fields/Field\[@Name='test-instance'\]/Value/text()")
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

class Defects(HPALM):
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

    def get_defects_all(self):
        url = "{base_url}/qcbin/rest/domains/{domain}/projects/{projects}/defects".format(base_url=self.base_url, domain=self.domain, projects=self.project)
        logger.debug(url)
        response = requests.get(url, headers=self.getheaders())
        logger.debug(response.headers)
        return response.status_code

    def get_defects_by_id(self, id):
        url = "{base_url}/qcbin/rest/domains/{domain}/projects/{projects}/defects/{id}".format(base_url=self.base_url, domain=self.domain, projects=self.project, id=id)
        logger.debug(url)
        response = requests.get(url, headers=self.getheaders())
        logger.debug(response.headers)
        return response.status_code

class TestSet(TestLab):
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

    def create_testset(self,path):
        raise ALMMethodNotImplementedException("Method not implemented")

    def delete_testset(self, path):
        raise ALMMethodNotImplementedException("Method not implemented")

class TestInstance(TestSet):
    def __init__(self):
        super(self.__class__, self).__init__()

    def create_ti(self, path):
        raise ALMMethodNotImplementedException("Method not implemented")

    def delete_ti(self, path):
        raise ALMMethodNotImplementedException("Method not implemented")

    def get_ti_run_id(self, domain, project, testset_id, test_id, test_ins):
        raise ALMMethodNotImplementedException("Method not implemented")

class Runs(TestInstance):
    def __init__(self, **kwargs):
        super(self.__class__, self).__init__(**kwargs)

    def create_runs(self, path):
        raise ALMMethodNotImplementedException("Method not implemented")

    def delete_runs(self, path):
        raise ALMMethodNotImplementedException("Method not implemented")

    def attach_file_runs(self, id, full_path):
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
        resp = requests.post(uri, params=ftext, headers=headers)
        if resp.status_code == 201:
            logger.info("Sucessfully attached file: %s size: %d" %(fname, len(ftext)))
        else:
            logger.error("Failed to create to attachement file: %s size: %d" %(fname, len(ftext)))
        return resp.status_code
    
    def get_attached_file(self, uri):
        headers = self.getheaders()
        uri = self.base_url + uri
        headers['Accept'] = 'application/octet-stream'
        resp = requests.get(uri, headers=headers)
        if resp.status_code == 200:
            logger.info("%s data read from file" %(resp.text))
