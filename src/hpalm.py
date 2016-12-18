#!/usr/bin/env python

"""
@author: Mallikarjunarao Kosuri
@email: Mallikarjunarao Kosuri <venkatamallikarjunarao.kosuri@adtran.com>
"""

import logging
import os
import requests
from requests.auth import HTTPBasicAuth

class ALMException(Exception):
    pass

logger = logging.getLogger(__name__)

def hp_alm_parser():
    """ Setup commandline parser """
    parser = argparse.ArgumentParser(prog="HP ALM",
                                     description="This program runs do some operation on HP ALM Server.",
                                     usage="%(prog)s [options]")

    # Subcommands
    commands = parser.add_subparsers(title="Commands", metavar='')

    # Common Options
    common_parser = argparse.ArgumentParser(add_help=False)

    # Common Options: Server Group
    group_server = common_parser.add_argument_group(title='Server Definition',
                                                    description='Define connection parameters for REST endpoint')
    group_server.add_argument("-ip", "--server-ip", type=str,
                              help="HP ALM server", default='')
    group_server.add_argument("-u", "--user", type=str,
                              help="Username.")                              )
    group_server.add_argument("-p", "--password", type=str,
                              help="Password")
    group_server.add_argument("-d", "--domain", type=str, help="Domain name")
    group_server.add_argument("-p", "--project", type=str, help="Project name")    
    
    return parser


class HPALM(object):
    headers = None
    def __init__(self, host, port=8080, username, password, domain, project):
        if host == None or port == None or username == None or \
                password == None or domain == None or project == None:
            raise ALMException("Please provide all mandatory params")
            
        self.base_url = 'http://' + host + ':' + port
        self.username = username
        self.password = password
        self.domain = domain
        self.project = project
        
    def getheaders(self):
        return self.headers
    
    def login(self):
        """
        Login into hp alm
        """
        headers = {'Content-Type' : 'application/xml'}
        authurl = self.base_url + '/qcbin/rest/is-authenticated'
        resp = requests.get(authurl, headers=headers)
        # print resp.headers
        # print resp.headers['WWW-Authenticate']
        lwssocookie = resp.headers['WWW-Authenticate']
        headers = {'Cookie' : lwssocookie}
        headers["Accept"] = 'application/xml'
        login_url = self.base_url + '/qcbin/authentication-point/authenticate'
        resp = requests.get(login_url, headers=headers, auth=HTTPBasicAuth(self.username, self.password))
        # print resp.headers
        qc_session = resp.headers['Set-Cookie']
        # print qc_session        
        cookie = ";".join((lwssocookie, qc_session))
        self.headers = {'content-type' : 'application/xml'}
        self.headers['accept'] = 'application/xml'
        self.headers['cookie'] = cookie
        if resp.status_code == 200:
            logger.info("%s  %s logged into alm" %(resp.status_code, self.username))
        else:
            raise ALMException("%s  %s failed to logging into HP ALM" %(resp.status_code, self.username))            
        return resp.status_code  
        
    def __del__(self):
        uri = self.base_url + '/qcbin/authentication-point/logout'
        resp = requests.get(uri, headers=self.headers)
        if resp.status_code == 200:
            logger.info("%s  %s logged out alm" %(resp.status_code, self.username))
        else:
            raise ALMException("%s  %s failed to loggedout from HP ALM" %(resp.status_code, self.username))            
        return resp.status_code
        
def text_xml(xml, xpath):
    dom_tree = etree.fromstring(xml)
    return dom_tree.xpath(xpath)

class TestLab(HPALM):
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
    def __init__(self):        
        pass;
    
    def run_attach_file(self, uri, report_id, full_path):
        """
        Attach file to test instance run
        """
        fd = None
        ftext = None
        if os.path.getsize(full_path) > 0:
            fd = open(full_path, "r")
            ftext = fd.read()
        else:
            raise ALMExcpetion("Unable to find file")
        # get filename    
        fname = os.path.basename(full_path)
        headers = self.getheaders()
        headers['content-type'] = 'application/octet-stream'
        headers['slug'] = fname
        uri = self.base_url + uri
        resp = requests.post(uri, params=ftext, headers=headers)
        if resp.status_code == 201:
            logger.info("Sucessfully attached file: %s size: %d" %(fname, len(ftext)))
        else:
            logger.error("Failed to create to attachement file: %s size: %d" %(fname, len(ftext)))
        return resp.status_code
    
    def run_get_attached_file(self, uri):
        """
        Get report attachment of given test instance        
        """
        headers = self.getheaders()
        _uri = self.base_url + uri
        headers['Accept'] = 'application/octet-stream'
        resp = requests.get(_uri, headers=headers)
        # if resp.status_code == 200:
            # logger.info("%s data read from file" %(

    def run_update_status(self, uri, status):
        """
        Modify existing report status i.e either Passed|Failed
        :param uri: HP ALM URI
        :param status: Needs to change report status
        :returns: sucess HTTP message
        """        
        for i in 2:
            if status == "Passed":
                status = "Failed"
                xml = "<Entity Type='run'><Fields><Field Name='status'><Value>" + status + "</Value></Field></Fields></Entity>"
                resp = requests.put(uri, params=xml, headers=self.getheaders())
            else:
                status = "Passed"
                xml = "<Entity Type='run'><Fields><Field Name='status'><Value>" + status + "</Value></Field></Fields></Entity>"
                resp = requests.put(uri, params=xml, headers=self.getheaders())
        
        return resp.status_code

    def tst_inst_get(tid):
        """
        This procedure will return list of test-instances in a given test set
        :param tid: integer test set identifier
        :returns: list test instances list
        """
        params = '{cycle-id[' + tid + ']}'
        url = self.base_url + '/qcbin/rest/domains/' + self.domain + '/projects/' + self.project + '/test-instances'
        response = requests.get(url, params=params, headers=self.getheaders())
        test_inst = text_xml(resp.content, "Entity/Fields/Field[@Name='test-instance']/Value/text()")
        return test_inst

    