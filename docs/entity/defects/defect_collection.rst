Defects Collection
==================

Description
-----------
The collection of Defects in the project.

URL
---
/qcbin/rest/domains/{domain}/projects/{project}/defects

Remarks
-------
To create a new defect, POST an XML compliant with the Entity Schema that contains definitions for all the required fields.

For bulk updates, deletions, and creation, see Bulk Operations.

HTTP Methods
------------
*GET*: Returns the collection of defects.

*PUT*: Bulk update with type=collection.

*DELETE*: Bulk deletion with type=collection.

*POST*: Creates a new defect resource. Bulk creation with type=collection. 

+----------------------------------+-----+-----+-------+------+
| Media Type                       | GET | PUT | DELTE | POST |
+==================================+=====+=====+=======+======+
| application/xml                  | YES | --  | --    | YES  |
+----------------------------------+-----+-----+-------+------+
| application/json                 | YES | --  | --    | YES  |
+----------------------------------+-----+-----+-------+------+
| application/xml;type=collection  | --  | YES | YES   | YES  |
+----------------------------------+-----+-----+-------+------+
| application/json;type=collection | --  | YES | YES   | YES  |
+----------------------------------+-----+-----+-------+------+

Returns
-------
One of the HTTP Return Codes.

On a GET operation, an XML string compliant with the Entities Collection Schema or a string containing the data in another supported format.

On a POST operation, the full data of the created defect in an XML string compliant with the Entity Schema or a string containing the data in another supported format.

GET Defects XML
---------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <!--
    GET: /qcbin/rest/domains/DOMAIN_NAME/projects/PROJECT_NAME/defects
    Accept: application/xml
    -->
    <Entities TotalResults="2">
        <Entity Type="defect">
            <Fields>
                <Field Name="has-change">
                    <Value/>
                </Field>
                <Field Name="planned-closing-ver">
                    <Value/>
                </Field>
                <Field Name="test-reference">
                    <Value/>
                </Field>
                <Field Name="subject">
                    <Value/>
                </Field>
                <Field Name="reproducible">
                    <Value/>
                </Field>
                <Field Name="request-id">
                    <Value/>
                </Field>
                <Field Name="data">
                    <Value/>
                </Field>
                <Field Name="request-server">
                    <Value/>
                </Field>
                <Field Name="id">
                    <Value>1</Value>
                </Field>
                <Field Name="others-linkage">
                    <Value>N</Value>
                </Field>
                <Field Name="description">
                    <Value/>
                </Field>
                <Field Name="priority">
                    <Value/>
                </Field>
                <Field Name="name">
                    <Value>Returned XML cannot be validated against XSD.</Value>
                </Field>
                <Field Name="run-reference">
                    <Value/>
                </Field>
                <Field Name="cycle-reference">
                    <Value/>
                </Field>
                <Field Name="dev-comments">
                    <Value/>
                </Field>
                <Field Name="creation-time">
                    <Value>2010-03-02</Value>
                </Field>
                <Field Name="to-mail">
                    <Value/>
                </Field>
                <Field Name="request-note">
                    <Value/>
                </Field>
                <Field Name="closing-version">
                    <Value/>
                </Field>
                <Field Name="cycle-id">
                    <Value/>
                </Field>
                <Field Name="detection-version">
                    <Value/>
                </Field>
                <Field Name="last-modified">
                    <Value>2010-03-04 14:30:00</Value>
                </Field>
                <Field Name="status">
                    <Value/>
                </Field>
                <Field Name="closing-date">
                    <Value/>
                </Field>
                <Field Name="linkage">
                    <Value>N</Value>
                </Field>
                <Field Name="detected-in-rcyc">
                    <Value/>
                </Field>
                <Field Name="detected-in-rel">
                    <Value/>
                </Field>
                <Field Name="severity">
                    <Value>2-Medium</Value>
                </Field>
                <Field Name="bug-ver-stamp">
                    <Value>1</Value>
                </Field>
                <Field Name="attachment">
                    <Value/>
                </Field>
                <Field Name="extended-reference">
                    <Value/>
                </Field>
                <Field Name="estimated-fix-time">
                    <Value/>
                </Field>
                <Field Name="target-rel">
                    <Value/>
                </Field>
                <Field Name="project">
                    <Value/>
                </Field>
                <Field Name="detected-by">
                    <Value>sa</Value>
                </Field>
                <Field Name="step-reference">
                    <Value/>
                </Field>
                <Field Name="owner">
                    <Value/>
                </Field>
                <Field Name="target-rcyc">
                    <Value/>
                </Field>
                <Field Name="actual-fix-time">
                    <Value/>
                </Field>
                <Field Name="request-type">
                    <Value/>
                </Field>
            </Fields>
        </Entity>
        <Entity Type="defect">
            <Fields>
                <Field Name="has-change">
                    <Value/>
                </Field>
                <Field Name="planned-closing-ver">
                    <Value/>
                </Field>
                <Field Name="test-reference">
                    <Value/>
                </Field>
                <Field Name="subject">
                    <Value/>
                </Field>
                <Field Name="reproducible">
                    <Value/>
                </Field>
                <Field Name="request-id">
                    <Value/>
                </Field>
                <Field Name="data">
                    <Value/>
                </Field>
                <Field Name="request-server">
                    <Value/>
                </Field>
                <Field Name="id">
                    <Value>2</Value>
                </Field>
                <Field Name="others-linkage">
                    <Value>N</Value>
                </Field>
                <Field Name="description">
                    <Value>Problem observed with temp lt 4 and humidity gt 60.</Value>
                </Field>
                <Field Name="priority">
                    <Value/>
                </Field>
                <Field Name="name">
                    <Value>Car does not start in cold weather.</Value>
                </Field>
                <Field Name="run-reference">
                    <Value/>
                </Field>
                <Field Name="cycle-reference">
                    <Value/>
                </Field>
                <Field Name="dev-comments">
                    <Value/>
                </Field>
                <Field Name="creation-time">
                    <Value>2010-03-02</Value>
                </Field>
                <Field Name="to-mail">
                    <Value/>
                </Field>
                <Field Name="request-note">
                    <Value/>
                </Field>
                <Field Name="closing-version">
                    <Value/>
                </Field>
                <Field Name="cycle-id">
                    <Value/>
                </Field>
                <Field Name="detection-version">
                    <Value/>
                </Field>
                <Field Name="last-modified">
                    <Value>2010-03-04 14:32:56</Value>
                </Field>
                <Field Name="status">
                    <Value/>
                </Field>
                <Field Name="closing-date">
                    <Value/>
                </Field>
                <Field Name="linkage">
                    <Value>N</Value>
                </Field>
                <Field Name="detected-in-rcyc">
                    <Value/>
                </Field>
                <Field Name="detected-in-rel">
                    <Value/>
                </Field>
                <Field Name="severity">
                    <Value>3-High</Value>
                </Field>
                <Field Name="bug-ver-stamp">
                    <Value>2</Value>
                </Field>
                <Field Name="attachment">
                    <Value/>
                </Field>
                <Field Name="extended-reference">
                    <Value/>
                </Field>
                <Field Name="estimated-fix-time">
                    <Value/>
                </Field>
                <Field Name="target-rel">
                    <Value/>
                </Field>
                <Field Name="project">
                    <Value/>
                </Field>
                <Field Name="detected-by">
                    <Value>sa</Value>
                </Field>
                <Field Name="step-reference">
                    <Value/>
                </Field>
                <Field Name="owner">
                    <Value/>
                </Field>
                <Field Name="target-rcyc">
                    <Value/>
                </Field>
                <Field Name="actual-fix-time">
                    <Value/>
                </Field>
                <Field Name="request-type">
                    <Value/>
                </Field>
            </Fields>
        </Entity>
    </Entities>

POST Defect XML
---------------

.. code-block:: xml

    <!--
    POST: /qcbin/rest/domains/DOMAIN_NAME/projects/PROJECT_NAME/defects
    Content-Type: application/xml
    -->
    <Entity Type="defect">
        <Fields>
            <Field Name="detected-by">
                <Value>sa</Value>
            </Field>
            <Field Name="creation-time">
                <Value>2010-03-02</Value>
            </Field>
            <Field Name="severity">
                <Value>2-Medium</Value>
            </Field>
            <Field Name="name">
                <Value>Returned XML cannot be validated against XSD.</Value>
            </Field>
        </Fields>
    </Entity>

