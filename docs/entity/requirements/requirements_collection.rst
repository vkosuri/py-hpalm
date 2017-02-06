Requirements Collection
=======================

Description
-----------
The collection of Requirements in the project.

URL
---
/qcbin/rest/domains/{domain}/projects/{project}/requirements

Remarks
-------
For bulk updates, deletions, and creation, see Bulk Operations.

Passing data in PUT or POST requests that contain fields that do not belong to the requirement's type is an error.

HTTP Methods
------------
*GET*: Retrieves the list of requirements.

*PUT*: Bulk update with type=collection.

*DELETE*: Bulk deletion with type=collection.

*POST*: Creates a new requirement. Bulk creation with type=collection.

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


GET requirements XML
--------------------

.. code-block:: xml

    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <!--
    GET: /qcbin/rest/domains/DOMAIN_NAME/projects/PROJECT_NAME/requirements
    Accept: application/xml
    -->
    <Entities TotalResults="5">
        <Entity Type="requirement">
            <Fields>
                <Field Name="vc-checkout-comments">
                    <Value/>
                </Field>
                <Field Name="rbt-analysis-setup-data">
                    <Value/>
                </Field>
                <Field Name="count">
                    <Value>0</Value>
                </Field>
                <Field Name="vc-checkin-time">
                    <Value/>
                </Field>
                <Field Name="vc-checkout-user-name">
                    <Value/>
                </Field>
                <Field Name="rbt-custom-testing-level">
                    <Value/>
                </Field>
                <Field Name="rbt-effective-bsns-impact">
                    <Value/>
                </Field>
                <Field Name="istemplate">
                    <Value>0</Value>
                </Field>
                <Field Name="rbt-bsns-impact">
                    <Value/>
                </Field>
                <Field Name="vc-version-number">
                    <Value>1</Value>
                </Field>
                <Field Name="comments">
                    <Value/>
                </Field>
                <Field Name="rbt-effective-fail-prob">
                    <Value/>
                </Field>
                <Field Name="request-status">
                    <Value/>
                </Field>
                <Field Name="request-updates">
                    <Value/>
                </Field>
                <Field Name="status">
                    <Value>N/A</Value>
                </Field>
                <Field Name="rbt-assessment-data">
                    <Value/>
                </Field>
                <Field Name="req-type">
                    <Value/>
                </Field>
                <Field Name="linkage">
                    <Value>N</Value>
                </Field>
                <Field Name="rbt-custom-fail-prob">
                    <Value/>
                </Field>
                <Field Name="order-id">
                    <Value>1</Value>
                </Field>
                <Field Name="rbt-testing-level">
                    <Value/>
                </Field>
                <Field Name="vc-checkin-date">
                    <Value/>
                </Field>
                <Field Name="parent-id">
                    <Value>-1</Value>
                </Field>
                <Field Name="target-rel">
                    <Value/>
                </Field>
                <Field Name="rbt-custom-risk">
                    <Value/>
                </Field>
                <Field Name="req-rich-content">
                    <Value/>
                </Field>
                <Field Name="owner">
                    <Value/>
                </Field>
                <Field Name="rbt-effective-risk">
                    <Value/>
                </Field>
                <Field Name="request-type">
                    <Value/>
                </Field>
                <Field Name="rbt-last-analysis-date">
                    <Value/>
                </Field>
                <Field Name="traced-from">
                    <Value>N</Value>
                </Field>
                <Field Name="no-of-sons">
                    <Value>1</Value>
                </Field>
                <Field Name="rbt-use-custom-risk">
                    <Value/>
                </Field>
                <Field Name="rbt-testing-hours">
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
                <Field Name="has-rich-content">
                    <Value/>
                </Field>
                <Field Name="request-assign-to">
                    <Value/>
                </Field>
                <Field Name="vc-checkout-date">
                    <Value/>
                </Field>
                <Field Name="traced-to">
                    <Value>N</Value>
                </Field>
                <Field Name="id">
                    <Value>0</Value>
                </Field>
                <Field Name="rbt-risk">
                    <Value/>
                </Field>
                <Field Name="rbt-effective-func-cmplx">
                    <Value/>
                </Field>
                <Field Name="name">
                    <Value>Requirements</Value>
                </Field>
                <Field Name="rbt-custom-testing-hours">
                    <Value/>
                </Field>
                <Field Name="vc-status">
                    <Value/>
                </Field>
                <Field Name="rbt-custom-func-cmplx">
                    <Value/>
                </Field>
                <Field Name="vc-checkin-user-name">
                    <Value/>
                </Field>
                <Field Name="creation-time">
                    <Value>2006-10-05</Value>
                </Field>
                <Field Name="rbt-use-custom-tl-and-te">
                    <Value/>
                </Field>
                <Field Name="request-note">
                    <Value/>
                </Field>
                <Field Name="req-ver-stamp">
                    <Value>4</Value>
                </Field>
                <Field Name="req-time">
                    <Value>14:34:58</Value>
                </Field>
                <Field Name="last-modified">
                    <Value>2010-03-15 11:55:58</Value>
                </Field>
                <Field Name="hierarchical-path">
                    <Value>AAA</Value>
                </Field>
                <Field Name="rbt-use-custom-bsns-impact">
                    <Value/>
                </Field>
                <Field Name="rbt-custom-bsns-impact">
                    <Value/>
                </Field>
                <Field Name="vc-checkout-time">
                    <Value/>
                </Field>
                <Field Name="type-id">
                    <Value>1</Value>
                </Field>
                <Field Name="attachment">
                    <Value/>
                </Field>
                <Field Name="vc-checkin-comments">
                    <Value/>
                </Field>
                <Field Name="rbt-rnd-estim-effort-hours">
                    <Value/>
                </Field>
                <Field Name="req-product">
                    <Value/>
                </Field>
                <Field Name="rbt-func-cmplx">
                    <Value/>
                </Field>
                <Field Name="rbt-use-custom-fail-prob">
                    <Value/>
                </Field>
                <Field Name="rbt-use-custom-func-cmplx">
                    <Value/>
                </Field>
                <Field Name="req-reviewed">
                    <Value>Not Reviewed</Value>
                </Field>
                <Field Name="rbt-analysis-result-data">
                    <Value/>
                </Field>
                <Field Name="target-rcyc">
                    <Value/>
                </Field>
                <Field Name="req-comment">
                    <Value/>
                </Field>
                <Field Name="req-priority">
                    <Value/>
                </Field>
                <Field Name="rbt-ignore-in-analysis">
                    <Value/>
                </Field>
                <Field Name="rbt-analysis-parent-req-id">
                    <Value/>
                </Field>
                <Field Name="rbt-fail-prob">
                    <Value/>
                </Field>
                <Field Name="father-name">
                    <Value/>
                </Field>
            </Fields>
        </Entity>
    </Entities>