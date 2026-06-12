## A — Header

- **Claim ID:** `OC-24-2203-1801-00002660-INVESTIGATOR6`
- **Job ID:** `JOB-B03A0BD4F469`
- **Run timestamp (UTC):** `20260611T185402Z`
- **Processing time:** `626` s
- **Documents:** requested=24, processed=24, failed=0
- **Facts extracted:** 546
- **Rules triggered:** 6

### Final fraud assessment

| metric | value |
| --- | --- |
| fraud_score | **85** |
| risk_category | **HIGH** |
| recommended_action | **FIELD** |

### Component scores (pre-fusion)

| signal | score (0–100) |
| --- | --- |
| rule_score | 92 |
| similarity_score | 44 |
| graph_score | 100 |
| consistency_score | 0 |
| ml_score | None |

> **Note on verdict:** the pipeline does NOT emit a binary fraud/not-fraud flag. The 'verdict' is the combination of `risk_category` (NO_RISK / LOW / MEDIUM / HIGH) and `recommended_action` (WAIVER / DESKTOP / FIELD). See Section J.6.

## B — Ingestion & classification

Total documents persisted: **24**

| original_filename | doc_id | doc_type | subtype | confidence | classifier | status | row_uuid |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 218890832_Registration_Certificate.jpg | 218890832_Registration_Certificate | vehicle_document | vehicle_document | 0.98 |  | PROCESSED | f37435ba-8179-4121-802f-3e350153c946 |
| 218890867_Motor_Driving_License_(MDL).jpg | 218890867_Motor_Driving_License_(MDL) | driving_license | driving_license | 0.98 |  | PROCESSED | 29fa1b55-1725-4bf7-a89a-8bbe207b0885 |
| 218890910_Claim_Form.jpg | 218890910_Claim_Form | claim_form | claim_form | 0.96 |  | PROCESSED | 0ac1836a-a639-4e52-9b0f-e7d5171d597f |
| 218890942_Claim_Form.jpg | 218890942_Claim_Form | correspondence | correspondence | 0.92 |  | PROCESSED | ee46df0a-c0e7-4b53-a91c-c85070d063f5 |
| 218890965_Repair_Estimate.jpg | 218890965_Repair_Estimate | repair_estimate | repair_estimate | 0.92 |  | PROCESSED | 069cc350-c68a-4f95-a341-4137e2e81ae1 |
| 218891028_Policy_Copy.jpg | 218891028_Policy_Copy | policy_copy | policy_copy | 0.96 |  | PROCESSED | f27c5c1c-88e9-45e7-91be-9ac9006b88d9 |
| 219032034_AML_Documents.jpg | 219032034_AML_Documents | pan_card | pan_card | 0.92 |  | PROCESSED | 179ff510-d8d7-431f-ba6a-de060bfc337b |
| 219032051_Claim_Form.jpg | 219032051_Claim_Form | correspondence | correspondence | 0.92 |  | PROCESSED | f2d4d85d-78f1-401c-a498-8e984fe5deaf |
| 219032145_Job_Card.jpg | 219032145_Job_Card | payment_slip | payment_slip | 0.92 |  | PROCESSED | ed09a6f1-9736-4c55-89b8-5117eaa9f7d7 |
| 219358654_Repair_Estimate.pdf | 219358654_Repair_Estimate | repair_estimate | repair_estimate | 0.98 |  | PROCESSED | e653a616-1acb-4378-b9c9-3b7e92e15655 |
| 219430367_Pre_Inspection_Photographs_Reports.PDF | 219430367_Pre_Inspection_Photographs_Reports | vehicle_document | vehicle_document | 0.92 |  | PROCESSED | 5daad72d-9ffa-48d3-8d54-ab627259ec12 |
| 222633146_Statement_of_Insured.pdf | 222633146_Statement_of_Insured | insured_statement | insured_statement | 0.78 |  | PROCESSED | 0c0a6982-7c61-4644-bfa4-2c99d0d4db57 |
| 222633187_Statement_of_Driver.pdf | 222633187_Statement_of_Driver | driver_statement | driver_statement | 0.88 |  | PROCESSED | dabf5699-218e-48d4-992e-a7594c785bf6 |
| 222633313_Vehicle_Damage_Photo.pdf | 222633313_Vehicle_Damage_Photo | photograph | photograph | 0.98 |  | PROCESSED | aa3ca302-8ecc-4bfc-acf7-9a24b12ed44c |
| 222633407_Spot_Photo_Sketch.pdf | 222633407_Spot_Photo_Sketch | photograph | photograph | 0.95 |  | PROCESSED | b24a6a1d-7def-49b2-b19f-c24ed87bdef7 |
| 222633435_Any_Other.pdf | 222633435_Any_Other | other | other | 0.45 |  | PROCESSED | d72d1318-419f-4d3b-990d-3c57c9854458 |
| 222696526_Statement_of_Insured.pdf | 222696526_Statement_of_Insured | insured_statement | insured_statement | 0.78 |  | PROCESSED | efac8d30-f46f-4eb0-9d11-437c83c2fb8b |
| 223214762_Investigation_Report.pdf | 223214762_Investigation_Report | correspondence | correspondence | 0.92 |  | PROCESSED | 5412926d-545c-40a3-a95e-08fe63391f61 |
| 223215102_Investigation_Report.pdf | 223215102_Investigation_Report | correspondence | correspondence | 0.92 |  | PROCESSED | 0ed4a2c3-1f68-4667-9090-f5abd921d8a9 |
| 223233211_Supplier_Bill.pdf | 223233211_Supplier_Bill | repair_estimate | repair_estimate | 0.92 |  | PROCESSED | ba1fdf22-196b-4f42-9518-054a3f8c757e |
| 223233267_Signed_Licensed_Surveyor_Report.pdf | 223233267_Signed_Licensed_Surveyor_Report | accident_report | accident_report | 0.92 |  | PROCESSED | c41badf1-19c5-4485-97b2-f56624fa837f |
| 223237590_Signed_Licensed_Surveyor_Report.pdf | 223237590_Signed_Licensed_Surveyor_Report | accident_report | accident_report | 0.92 |  | PROCESSED | 77eb42f1-c639-40a6-a92c-42a2ac9ca221 |
| 223404609_Follow-up_Letters.pdf | 223404609_Follow-up_Letters | correspondence | correspondence | 0.92 |  | PROCESSED | d840dc4f-a181-4f72-b0ce-f255a9bdc49f |
| 223721550_Follow-up_Letters.jpg | 223721550_Follow-up_Letters | correspondence | correspondence | 0.95 |  | PROCESSED | 175c77eb-c1b3-4e13-bb88-0c420c2abee3 |

## C — Extracted fields

### Doc `218890832_Registration_Certificate` — `vehicle_document`  (row uuid `f37435ba-8179-4121-802f-3e350153c946`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| amount | 200 |  |  | 551c2d54-525a-5fa4-8487-3714ade8492a | ingest.documents.raw_extraction |
| address | Surat |  |  | 54956e21-3263-5770-ad62-025471d179a0 | ingest.documents.raw_extraction |
| amount_2 | 20634 |  |  | 769f23ec-9df5-56ba-a28c-7c5c7fd925ac | ingest.documents.raw_extraction |
| amount_3 | 814.00 |  |  | e6a0f5b2-3f31-5633-8be0-49dfaed6d094 | ingest.documents.raw_extraction |
| location | Gujarat |  |  | 9fcf74bb-a76b-5b27-b049-c0583008e1d3 | ingest.documents.raw_extraction |
| person_name | MAHESH KUMAR |  |  | f031d491-8be2-5218-a9d7-fcaeefab8dc3 | ingest.documents.raw_extraction |
| company_name | BAJAJ FINANCE LIMITED |  |  | cdbed2f8-efde-549e-b0e7-c19b51cabbf0 | ingest.documents.raw_extraction |
| insurer_name | Bajaj Allianz General Insurance Co. Ltd. |  |  | e79bd31f-68e8-5ab7-bcd4-10ba696a9848 | ingest.documents.raw_extraction |
| phone_number | 9727635960 |  |  | edbd38b3-a35c-5aee-b87e-773de51ca6e3 | ingest.documents.raw_extraction |
| tax_and_fees | {"tax_paid_upto": "One Time", "cash_receipt_date": "2023-08-08", "cash_receipt_number": "GJ230808C9783109", "particular_fee_amount": 200, "particular_fee_currency": "INR"} |  | {'tax_paid_upto': 'One Time', 'cash_receipt_date': '2023-08-08', 'cash_receipt_number': 'GJ230808C9783109', 'particular_fee_amount': 200, 'particular_fee_currency': 'INR'} | 4aabf8b7-ab11-5c0d-a2d4-881b6bde9e17 | ingest.documents.raw_extraction |
| engine_number | G3H4DM199755 |  |  | 20afd3d5-f5a7-53ff-a1fb-b0bd921822e6 | ingest.documents.raw_extraction |
| owner_details | {"owner_name": "MAHESH KUMAR", "owner_address": "C/O NEW VARGHIA HOUSING SOCIETY(KAMREJ) ROAD DHAL, Surat Gujarat-395006", "owner_name_original_script": "MAHESH KUMAR", "owner_address_original_script… |  | {'owner_name': 'MAHESH KUMAR', 'owner_address': 'C/O NEW VARGHIA HOUSING SOCIETY(KAMREJ) ROAD DHAL, Surat Gujarat-395006', 'owner_name_original_script': 'MAHESH KUMAR', 'owner_address_original_script… | 09a1af78-134a-55c3-86bd-94a0c5c8f9af | ingest.documents.raw_extraction |
| policy_number | OG-24-2203-1801-0005412 |  |  | c8945762-dbd1-5c59-b17c-87ec552485c9 | ingest.documents.raw_extraction |
| chassis_number | MALASIYALDA226944 |  |  | ab838704-e5e4-533b-a08e-d726f180481a | ingest.documents.raw_extraction |
| receipt_number | GJ230808C9783109 |  |  | 20d50f0d-6952-54ee-af07-8278a0bd8db7 | ingest.documents.raw_extraction |
| vehicle_status | {"status": "Active", "last_change_of_address_done_on": null, "last_alteration_of_vehicle_done_on": null} |  | {'status': 'Active', 'last_change_of_address_done_on': None, 'last_alteration_of_vehicle_done_on': None} | 1266d20b-da28-57d1-80be-08689d82edd8 | ingest.documents.raw_extraction |
| contact_details | {"email_id": null, "mobile_number": "9727635960"} |  | {'email_id': None, 'mobile_number': '9727635960'} | 6bf55dc5-3ae4-5d44-80e2-7d1a4b1c40c6 | ingest.documents.raw_extraction |
| finance_details | {"finance_type": "One Time", "financer_name": "BAJAJ FINANCE LIMITED", "financer_address": "OFFICE 301 TO 311 3RD FL, UNIVERSALBUSINESS CENTER L.P.SAVANI ROADNEAR MADHURAM CIRCLE ADAJAN, Surat-395009… |  | {'finance_type': 'One Time', 'financer_name': 'BAJAJ FINANCE LIMITED', 'financer_address': 'OFFICE 301 TO 311 3RD FL, UNIVERSALBUSINESS CENTER L.P.SAVANI ROADNEAR MADHURAM CIRCLE ADAJAN, Surat-395009… | 9b476a8d-8ca9-5d78-bb14-740bb29d9bd1 | ingest.documents.raw_extraction |
| vehicle_details | {"body_type": "C/W-PETROL", "fuel_type": "PETROL", "tax_amount": 20634, "horse_power": 831, "vehicle_make": "HYUNDAI MOTOR INDIA LTD", "engine_number": "G3H4DM199755", "vehicle_class": "INDRASING VAS… |  | {'body_type': 'C/W-PETROL', 'fuel_type': 'PETROL', 'tax_amount': 20634, 'horse_power': 831, 'vehicle_make': 'HYUNDAI MOTOR INDIA LTD', 'engine_number': 'G3H4DM199755', 'vehicle_class': 'INDRASING VAS… | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 | ingest.documents.raw_extraction |
| insurance_details | {"insurance_company": "Bajaj Allianz General Insurance Co. Ltd.", "insurance_valid_from": "2023-08-03", "insurance_valid_upto": "2024-08-02", "policy_certificate_number": "OG-24-2203-1801-0005412"} |  | {'insurance_company': 'Bajaj Allianz General Insurance Co. Ltd.', 'insurance_valid_from': '2023-08-03', 'insurance_valid_upto': '2024-08-02', 'policy_certificate_number': 'OG-24-2203-1801-0005412'} | d3ce9a87-d817-52e0-ad05-e0e3f85353e9 | ingest.documents.raw_extraction |
| organization_name | HYUNDAI MOTOR INDIA LTD |  |  | c5e5ee24-ebd6-5d5a-bbb6-f8b01cb36237 | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AK0736 |  |  | cb053bad-36eb-5b9e-a1ca-cea5d70d2c8d | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "Header", "field_label": "Application No", "field_value": "GJ230808V2160368"}, {"section": "Vehicle Particulars", "field_label": "Previous Registration No", "field_value": null}, {"secti… |  | [{'section': 'Header', 'field_label': 'Application No', 'field_value': 'GJ230808V2160368'}, {'section': 'Vehicle Particulars', 'field_label': 'Previous Registration No', 'field_value': None}, {'secti… | 189290e2-bf97-5918-a399-2d60b5116213 | ingest.documents.raw_extraction |
| application_number_for_registration | GJ230808V2160368 |  |  | 526778ec-b1fd-54bc-838d-aef5144ac7fe | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `218890867_Motor_Driving_License_(MDL)` — `driving_license`  (row uuid `29fa1b55-1725-4bf7-a89a-8bbe207b0885`)

**Fields (extracted_fields / raw_extraction JSONB):**

> _(no rows)_

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json
{
  "dl_details": {
    "name": null,
    "address": null,
    "badge_no": null,
    "s_d_w_of": null,
    "badge_date": null,
    "blood_group": null,
    "office_code": null,
    "organ_donar": null,
    "old_rto_name": null,
    "reference_no": null,
    "date_of_birth": null,
    "date_of_issue": null,
    "dl_valid_from": null,
    "hill_validity": null,
    "date_of_expiry": null,
    "license_number": null,
    "old_license_no": null,
    "photo_of_holder": null,
    "type_of_license": null,
    "issuing_authority": null,
    "hazardous_validity": null,
    "date_of_first_issue": null,
    "signature_of_holder": null,
    "state_driving_licence_name": null,
    "signature_of_issuing_authority": null,
    "class_of_vehicle_authorized_to_drive": null,
    "additional_endorsement_of_dl_aed_date": null
  }
}
```

### Doc `218890910_Claim_Form` — `claim_form`  (row uuid `0ac1836a-a639-4e52-9b0f-e7d5171d597f`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| date | 2025-04-10 |  |  | c8bd3410-27c4-5697-ab31-930e56095b9c | ingest.documents.raw_extraction |
| location | BIHAR |  |  | 6d827c66-88ee-5564-a2a6-c72d4232a47d | ingest.documents.raw_extraction |
| dl_number | [HANDWRITTEN: UJOSIO0 2HADI061] |  |  | c19564fc-51aa-563b-9525-5b838a24f812 | ingest.documents.raw_extraction |
| declaration | {"date": "2025-04-10", "insured_name": "[HANDWRITTEN: MAHA 3 HDYAR]", "declarant_name": "[HANDWRITTEN: MAHA 3 HDYAR]", "signature_present": true} |  | {'date': '2025-04-10', 'insured_name': '[HANDWRITTEN: MAHA 3 HDYAR]', 'declarant_name': '[HANDWRITTEN: MAHA 3 HDYAR]', 'signature_present': True} | 7507bea6-3ec6-5ac3-a00a-a43811a71348 | ingest.documents.raw_extraction |
| driver_name | [HANDWRITTEN: FIR HADI H HDYAR ISHAHDI] |  |  | 41b2536e-723c-5262-aa53-9b1967335651 | ingest.documents.raw_extraction |
| person_name | [HANDWRITTEN: MAHA 3 HDYAR] |  |  | 425914a8-7792-5126-a99d-ec03bf364f94 | ingest.documents.raw_extraction |
| insured_name | [HANDWRITTEN: DRAM E3 H HDYAR] |  |  | be7dbba9-b9da-5f65-b521-63dc7dca1bdd | ingest.documents.raw_extraction |
| insurer_name | Bajaj Allianz General Insurance Company Limited |  |  | a21d933b-61fe-5530-b656-27dedbc1acc4 | ingest.documents.raw_extraction |
| phone_number | [HANDWRITTEN: 2ND0245 HN] |  |  | 28261d56-f1f1-5042-a297-bd02b0a3eab2 | ingest.documents.raw_extraction |
| policy_number | OC-24-9003-1801-0000 2660 |  |  | ed6f71e3-59b5-5452-b8e1-3e1b5c775bb9 | ingest.documents.raw_extraction |
| chassis_number | [HANDWRITTEN: 2102 2029] |  |  | 81d95289-ce1e-5aa7-bc00-f115e1600f07 | ingest.documents.raw_extraction |
| driver_details | {"dl_number": "[HANDWRITTEN: UJOSIO0 2HADI061]", "dl_valid_to": null, "driver_name": "[HANDWRITTEN: FIR HADI H HDYAR ISHAHDI]", "issuing_rto": "[HANDWRITTEN: UJSLO7]", "dl_valid_from": null, "driver_… |  | {'dl_number': '[HANDWRITTEN: UJOSIO0 2HADI061]', 'dl_valid_to': None, 'driver_name': '[HANDWRITTEN: FIR HADI H HDYAR ISHAHDI]', 'issuing_rto': '[HANDWRITTEN: UJSLO7]', 'dl_valid_from': None, 'driver_… | 283f6cfc-c1f3-51d9-90aa-1e7ecc8e04ff | ingest.documents.raw_extraction |
| addon_endorsement | {"ncb_protect": null, "other_addons": [], "engine_protect": null, "nil_depreciation": null, "consumables_cover": null, "roadside_assistance": null} |  | {'ncb_protect': None, 'other_addons': [], 'engine_protect': None, 'nil_depreciation': None, 'consumables_cover': None, 'roadside_assistance': None} | 3e243ac4-a586-5090-990f-56c2be24f2f2 | ingest.documents.raw_extraction |
| bank_neft_details | {"branch": null, "bank_name": null, "ifsc_code": null, "micr_code": null, "proof_type": null, "account_type": null, "account_number": null, "account_holder_name": null} |  | {'branch': None, 'bank_name': None, 'ifsc_code': None, 'micr_code': None, 'proof_type': None, 'account_type': None, 'account_number': None, 'account_holder_name': None} | 60e1c056-c151-55ad-aa6f-a65d604cbe45 | ingest.documents.raw_extraction |
| incident_location | [HANDWRITTEN: Nema Vasselley city] |  |  | 6a0d3ddc-3b6f-59b3-a578-248116d49115 | ingest.documents.raw_extraction |
| incident_narrative | {"damaged_parts": [], "incident_type": null, "illegible_portions": [{"context": "Handwritten in regional script, multiple words unclear", "position": "Section 5 - entire narrative block"}], "original… |  | {'damaged_parts': [], 'incident_type': None, 'illegible_portions': [{'context': 'Handwritten in regional script, multiple words unclear', 'position': 'Section 5 - entire narrative block'}], 'original… | 29d0dab6-e02b-530e-b28c-0dd2b59fd45c | ingest.documents.raw_extraction |
| third_party_details | {"tp_entries": []} |  | {'tp_entries': []} | 0bdabd6b-f1a0-52a0-83c7-f249d5e611e7 | ingest.documents.raw_extraction |
| policyholder_details | {"city": "[HANDWRITTEN: GUNAMI]", "email": "[HANDWRITTEN: GUNAMI]", "state": "[HANDWRITTEN: BIHAR]", "address": "[HANDWRITTEN: GUNAMI VORBAD 4]", "pin_code": "[HANDWRITTEN: 841601]", "pan_number": nu… |  | {'city': '[HANDWRITTEN: GUNAMI]', 'email': '[HANDWRITTEN: GUNAMI]', 'state': '[HANDWRITTEN: BIHAR]', 'address': '[HANDWRITTEN: GUNAMI VORBAD 4]', 'pin_code': '[HANDWRITTEN: 841601]', 'pan_number': No… | 44c22391-dbd2-564c-bb8e-683a2eafdd79 | ingest.documents.raw_extraction |
| vehicle_registration | CA 2 #AA 0#36 |  |  | 4469a6d2-9c66-53da-a5ff-105956a12619 | ingest.documents.raw_extraction |
| accident_loss_details | {"accident_date": "[HANDWRITTEN: 2102 2029]", "accident_time": "[HANDWRITTEN: 1913 0 pm]", "engine_number": null, "gd_fir_number": null, "chassis_number": "[HANDWRITTEN: 2102 2029]", "nature_of_loss"… |  | {'accident_date': '[HANDWRITTEN: 2102 2029]', 'accident_time': '[HANDWRITTEN: 1913 0 pm]', 'engine_number': None, 'gd_fir_number': None, 'chassis_number': '[HANDWRITTEN: 2102 2029]', 'nature_of_loss'… | ad47b3e7-bb65-5557-9846-d478bc6a2c74 | ingest.documents.raw_extraction |
| pin_code_from_section_2 | [HANDWRITTEN: 841601] |  |  | 428738d7-5801-5617-b66a-89035e188d9d | ingest.documents.raw_extraction |
| form_completion_metadata | {"sections_blank": ["Section 6 - Add-on Endorsement", "Section 7 - Third Party Details", "Section 8 - Bank NEFT Details"], "checkbox_states": [{"section": "3", "all_options": ["Yes", "No"], "field_la… |  | {'sections_blank': ['Section 6 - Add-on Endorsement', 'Section 7 - Third Party Details', 'Section 8 - Bank NEFT Details'], 'checkbox_states': [{'section': '3', 'all_options': ['Yes', 'No'], 'field_la… | cf3e91d0-682f-5cd5-9b20-3f3a41b8efcc | ingest.documents.raw_extraction |
| cross_section_verification | {"name_match": {"match": false, "section_2_name": "[HANDWRITTEN: DRAM E3 H HDYAR]", "section_9_name": "[HANDWRITTEN: MAHA 3 HDYAR]"}, "pin_vs_state": {"plausible": true, "pin_prefix": "84", "stated_s… |  | {'name_match': {'match': False, 'section_2_name': '[HANDWRITTEN: DRAM E3 H HDYAR]', 'section_9_name': '[HANDWRITTEN: MAHA 3 HDYAR]'}, 'pin_vs_state': {'plausible': True, 'pin_prefix': '84', 'stated_s… | 03080231-7995-5412-8f93-1b0aef1c6706 | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "Section 2", "field_label": "Cover Note No", "field_value": null}, {"section": "Section 3", "field_label": "Number of Occupants", "field_value": "02"}, {"section": "Section 3", "field_la… |  | [{'section': 'Section 2', 'field_label': 'Cover Note No', 'field_value': None}, {'section': 'Section 3', 'field_label': 'Number of Occupants', 'field_value': '02'}, {'section': 'Section 3', 'field_la… | aa83e587-764c-5dd1-8335-463a5e6b88b4 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `218890942_Claim_Form` — `correspondence`  (row uuid `ee46df0a-c0e7-4b53-a91c-c85070d063f5`)

**Fields (extracted_fields / raw_extraction JSONB):**

> _(no rows)_

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `218890965_Repair_Estimate` — `repair_estimate`  (row uuid `069cc350-c68a-4f95-a341-4137e2e81ae1`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| totals | {"currency": "INR", "grand_total": "[illegible]", "total_labor": "FRT", "total_paint": 8000, "total_parts": "APPROVED"} |  | {'currency': 'INR', 'grand_total': '[illegible]', 'total_labor': 'FRT', 'total_paint': 8000, 'total_parts': 'APPROVED'} | b6e61f8e-9ac2-5af2-a39d-078771fcf49d | ingest.documents.raw_extraction |
| labor_list | [{"description": "Front Bumper O & R", "serial_number": 17, "operation_type": "O & R", "approval_status": "FRT"}, {"description": "Rearrest Pummel O & R", "serial_number": 18, "operation_type": "O & … |  | [{'description': 'Front Bumper O & R', 'serial_number': 17, 'operation_type': 'O & R', 'approval_status': 'FRT'}, {'description': 'Rearrest Pummel O & R', 'serial_number': 18, 'operation_type': 'O & … | 1ad44263-8ccb-511a-aff9-3369e918684d | ingest.documents.raw_extraction |
| paint_list | [{"total": 8000, "currency": "INR", "description": "Touching Dyed", "serial_number": 23}] |  | [{'total': 8000, 'currency': 'INR', 'description': 'Touching Dyed', 'serial_number': 23}] | 3ee7778a-0e21-5d33-8a61-a9de553f8303 | ingest.documents.raw_extraction |
| parts_list | [{"status": "NEW", "quantity": 1, "part_type": "Plastic", "description": "Front Bumper", "serial_number": 1, "approval_status": "APPROVED"}, {"status": "NEW", "quantity": 1, "part_type": "Plastic", "… |  | [{'status': 'NEW', 'quantity': 1, 'part_type': 'Plastic', 'description': 'Front Bumper', 'serial_number': 1, 'approval_status': 'APPROVED'}, {'status': 'NEW', 'quantity': 1, 'part_type': 'Plastic', '… | 1bf8e66c-3d52-54f9-8e12-0bf3c5255826 | ingest.documents.raw_extraction |
| document_date | 2023-08-09 |  |  | 5dec1c3c-3916-5727-966d-8f059a56d791 | ingest.documents.raw_extraction |
| vendor_details | {"vendor_name": "Navjivan Motors Pvt. Ltd.", "branch_phone": "(0261) 2855 777, 2858 777", "vendor_email": "bodyshop@navjivanhydundai.com", "branch_office": "Tulsi Krupa Arcade, Bis. Dr. House, Parvat… |  | {'vendor_name': 'Navjivan Motors Pvt. Ltd.', 'branch_phone': '(0261) 2855 777, 2858 777', 'vendor_email': 'bodyshop@navjivanhydundai.com', 'branch_office': 'Tulsi Krupa Arcade, Bis. Dr. House, Parvat… | c65231ed-aca0-5f43-8a7d-a6f09b72cc2e | ingest.documents.raw_extraction |
| document_number | 230 |  |  | 029a72f8-7839-563a-b1f4-cfdf7bc87cf5 | ingest.documents.raw_extraction |
| vehicle_details | {"make": "Hyundai", "color": "White", "model": "EON", "engine_number": "[illegible]", "chassis_number": "[illegible]", "registration_number": "GJ 9 2 4 A A 0436"} |  | {'make': 'Hyundai', 'color': 'White', 'model': 'EON', 'engine_number': '[illegible]', 'chassis_number': '[illegible]', 'registration_number': 'GJ 9 2 4 A A 0436'} | 8ae4bff9-02e8-594a-bde1-60156f25f484 | ingest.documents.raw_extraction |
| customer_details | {"customer_name": "Mahesh Khoei Vasava", "customer_address": "[illegible]"} |  | {'customer_name': 'Mahesh Khoei Vasava', 'customer_address': '[illegible]'} | b87ff850-bce1-5db7-9671-4fe3c78c1cab | ingest.documents.raw_extraction |
| insurance_linkage | {"claim_number": "[illegible]", "policy_number": "[illegible]", "insurance_company": "Bajaj Allianz", "authorization_number": "[illegible]"} |  | {'claim_number': '[illegible]', 'policy_number': '[illegible]', 'insurance_company': 'Bajaj Allianz', 'authorization_number': '[illegible]'} | 0fb92b74-8c4e-580f-aa01-6991d284ae02 | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"field_label": "Document Copy Type", "field_value": "Customer / Insurance Co. Copy"}, {"field_label": "Surveyed by", "field_value": "[illegible]"}, {"field_label": "Reinspection by", "field_value":… |  | [{'field_label': 'Document Copy Type', 'field_value': 'Customer / Insurance Co. Copy'}, {'field_label': 'Surveyed by', 'field_value': '[illegible]'}, {'field_label': 'Reinspection by', 'field_value':… | acf08aaf-0207-5a6d-b0ab-1d01f5477f4b | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `218891028_Policy_Copy` — `policy_copy`  (row uuid `f27c5c1c-88e9-45e7-91be-9ac9006b88d9`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| date | 03-AUG-2023 |  |  | c45e5a8f-32ee-5330-aee1-ef0746cee69b | ingest.documents.raw_extraction |
| gstin | 24AABCB5730G1Z3 |  |  | 37945fed-5adb-5b19-9881-6f69d0e08cb4 | ingest.documents.raw_extraction |
| amount | 200000.00 |  |  | ac3a290c-0942-5945-af0c-0ee051c707f9 | ingest.documents.raw_extraction |
| date_2 | 02-AUG-2024 |  |  | 516f870e-b7af-5919-8e86-d734503c2df5 | ingest.documents.raw_extraction |
| address | Surat |  |  | 7bad1733-bf8e-52d9-a67c-f5f174d27527 | ingest.documents.raw_extraction |
| amount_2 | 3031.00 |  |  | 180166a9-bdba-505a-aecd-331e648e679f | ingest.documents.raw_extraction |
| amount_3 | 2094.00 |  |  | 87cd1df7-766a-5416-8891-befd42a773a3 | ingest.documents.raw_extraction |
| amount_4 | 6792.00 |  |  | 0b5ba352-b1fd-53a1-96b8-536a75c61306 | ingest.documents.raw_extraction |
| address_2 | Gujarat |  |  | 8305f8ac-6233-542a-8abd-2fb5ce10804a | ingest.documents.raw_extraction |
| issue_date | 02-AUG-2023 |  |  | 499a469e-98cb-5c03-b0ba-4529962faf1c | ingest.documents.raw_extraction |
| pan_number | AABCB5730G |  |  | dac20136-ad6d-53a0-9e5e-cf8a693637d1 | ingest.documents.raw_extraction |
| insured_name | MAHESHKUMAR INDRASING VASAVA |  |  | 9359f38c-16bb-539a-9156-b5378f397d1b | ingest.documents.raw_extraction |
| insurer_name | BAJAJ ALLIANZ GENERAL INSURANCE COMPANY LIMITED |  |  | 4fd78460-e555-5e90-bef2-ff10dad05fe8 | ingest.documents.raw_extraction |
| phone_number | 0261-2256882 |  |  | 1768ed11-a4ad-5e58-ab00-823b13869952 | ingest.documents.raw_extraction |
| engine_number | G3HADM199755 |  |  | f2ac6f6b-b0b6-57e0-a383-79984bbae18e | ingest.documents.raw_extraction |
| policy_number | OG-24-2203-1801-00005412 |  |  | 8256265f-bda3-59c3-b052-5797d78ce904 | ingest.documents.raw_extraction |
| chassis_number | MALA351ALDM226944 |  |  | e4796257-98c5-57c6-a475-b7dc69136521 | ingest.documents.raw_extraction |
| invoice_number | 588338246/1 |  |  | c381d22d-19ec-5718-ba78-05dfa9561971 | ingest.documents.raw_extraction |
| policy_details | {"gvw": null, "uin": "IRDAN113RP00251V01200102", "make": "HYUNDAI", "zone": null, "email": null, "gstin": "24AABCB5730G1Z3", "model": "EON", "product": "PRIVATE CAR PACKAGE POLICY", "trailer": "-,-",… |  | {'gvw': None, 'uin': 'IRDAN113RP00251V01200102', 'make': 'HYUNDAI', 'zone': None, 'email': None, 'gstin': '24AABCB5730G1Z3', 'model': 'EON', 'product': 'PRIVATE CAR PACKAGE POLICY', 'trailer': '-,-',… | 21560b49-debb-5c2d-b869-04129a63d7f4 | ingest.documents.raw_extraction |
| organization_name | BAJAJ FINANCE LIMITED |  |  | 2388f7f0-f036-5dd2-ab38-8164d19d4481 | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AA0736 |  |  | f499d7f7-de0e-5d2f-a7e9-5778288d5b76 | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "Vehicle Details", "field_label": "Hypothecation Details", "field_value": "BAJAJ FINANCE LIMITED", "field_label_original_script": "Hypothecation Details", "field_value_original_script": … |  | [{'section': 'Vehicle Details', 'field_label': 'Hypothecation Details', 'field_value': 'BAJAJ FINANCE LIMITED', 'field_label_original_script': 'Hypothecation Details', 'field_value_original_script': … | 553584ea-bc9d-5fd5-87e7-c47279f01fef | ingest.documents.raw_extraction |
| customer_identification_number | 399252385 |  |  | 39f5eece-6ff0-5880-84ca-65aabd996763 | ingest.documents.raw_extraction |
| irdai_unique_identification_number | IRDAN113RP00251V01200102 |  |  | 8a3800b8-685c-5404-a06f-4a30c182806a | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json
{
  "policy_details": {
    "gvw": null,
    "uin": "IRDAN113RP00251V01200102",
    "make": "HYUNDAI",
    "zone": null,
    "email": null,
    "gstin": "24AABCB5730G1Z3",
    "model": "EON",
    "product": "PRIVATE CAR PACKAGE POLICY",
    "trailer": "-,-",
    "elec_acc": "0",
    "sub_type": "SPORTZ",
    "expiry_on": "2024-08-02",
    "fuel_type": null,
    "contact_no": "0261-2256882",
    "invoice_no": "588338246/1",
    "agency_code": null,
    "agency_name": null,
    "customer_id": "399252385",
    "scrutiny_no": null,
    "vehcile_idv": "2,00,000.00",
    "channel_name": null,
    "cng_lpg_unit": "0",
    "insured_name": "MAHESHKUMAR INDRASING VASAVA",
    "nominee_name": null,
    "non_elec_acc": "0",
    "cover_note_no": null,
    "engine_number": "G3HADM199755",
    "policy_number": "OG-24-2203-1801-00005412",
    "policy_status": "Active",
    "chassis_number": "MALA351ALDM226944",
    "company_gst_no": "24AABCB5730G1Z3",
    "company_pan_no": "AABCB5730G",
    "no_claim_bonus": "0%",
    "receipt_number": null,
    "transaction_id": null,
    "policy_end_date": "2024-08-02",
    "previous_insuer": null,
    "proposer_number": "0261-2256882",
    "manufacture_year": "
```

### Doc `219032034_AML_Documents` — `pan_card`  (row uuid `179ff510-d8d7-431f-ba6a-de060bfc337b`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| pan_number | BOTPV1228N |  |  | 54aded9a-4ef0-5a68-ae8c-1d556b787065 | ingest.documents.raw_extraction |
| father_name | INDRASING DIVEJIYABHAI VASAVA |  |  | c62b6bb7-b8cd-56f9-bea8-73ff4ab07678 | ingest.documents.raw_extraction |
| pan_details | {"address": null, "date_of_birth": null, "father_s_name": "INDRASING DIVEJIYABHAI VASAVA", "holder_s_name": "BHRIKUMAR INDRASING VASAVA", "pan_card_number": "BOTPV1228N", "validity_status": null, "is… |  | {'address': None, 'date_of_birth': None, 'father_s_name': 'INDRASING DIVEJIYABHAI VASAVA', 'holder_s_name': 'BHRIKUMAR INDRASING VASAVA', 'pan_card_number': 'BOTPV1228N', 'validity_status': None, 'is… | b4790284-da4f-5720-a039-71157369460f | ingest.documents.raw_extraction |
| person_name | BHRIKUMAR INDRASING VASAVA |  |  | 8af252d8-fc7a-523c-abbe-008e8485f499 | ingest.documents.raw_extraction |
| organization_name | Income Tax Department |  |  | 03f94ffb-4c01-553a-9af9-e698b668c808 | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "pan_details", "field_label": "Document Type Label", "field_value": "Permanent Account Number Card", "field_label_original_script": "\u0938\u094d\u0925\u093e\u092f\u0940 \u0916\u093e\u09… |  | [{'section': 'pan_details', 'field_label': 'Document Type Label', 'field_value': 'Permanent Account Number Card', 'field_label_original_script': 'स्थायी खाता संख्या कार्ड', 'field_value_original_scri… | ecacd7ff-c41b-569d-a681-472d166be33a | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json
{
  "pan_details": {
    "address": null,
    "date_of_birth": null,
    "father_s_name": "INDRASING DIVEJIYABHAI VASAVA",
    "holder_s_name": "BHRIKUMAR INDRASING VASAVA",
    "pan_card_number": "BOTPV1228N",
    "validity_status": null,
    "issuing_authority": "Income Tax Department, Government of India",
    "signature_of_holder": "Signature present (handwritten)"
  }
}
```

### Doc `219032051_Claim_Form` — `correspondence`  (row uuid `f2d4d85d-78f1-401c-a498-8e984fe5deaf`)

**Fields (extracted_fields / raw_extraction JSONB):**

> _(no rows)_

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `219032145_Job_Card` — `payment_slip`  (row uuid `ed09a6f1-9736-4c55-89b8-5117eaa9f7d7`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| amount | 2000 |  |  | 99fca8fc-ffbf-5731-a32b-3a3a3f7f23ac | ingest.documents.raw_extraction |
| location | Surat |  |  | e3d062ac-3b4e-5db8-9928-eea3f7e10cf4 | ingest.documents.raw_extraction |
| person_name | Vikesh Patil |  |  | 540352f1-699b-5a08-a6bb-143e7835263d | ingest.documents.raw_extraction |
| phone_number | 9727635980 |  |  | 9765aed9-958f-5044-b324-ef3db07939c5 | ingest.documents.raw_extraction |
| person_name_2 | Nana Varaziha |  |  | 50d76286-cd6f-5c8c-8c97-177a4a0b8c85 | ingest.documents.raw_extraction |
| gate_pass_details | {"amount": "2000", "time_in": "10:45 PM", "currency": "INR", "time_out": "[blank]", "pass_type": "E.R.S. Gate Pass", "issue_date": "2023-08-09", "pass_number": "1800", "driven_by_signature": "[presen… |  | {'amount': '2000', 'time_in': '10:45 PM', 'currency': 'INR', 'time_out': '[blank]', 'pass_type': 'E.R.S. Gate Pass', 'issue_date': '2023-08-09', 'pass_number': '1800', 'driven_by_signature': '[presen… | efd36176-272d-58db-bdbc-391c3dea7755 | ingest.documents.raw_extraction |
| organization_name | Navjivan Motors Pvt. Ltd. |  |  | 8fb25af8-d434-59b1-bdf7-288aec56ef5d | ingest.documents.raw_extraction |
| vehicle_registration | GH27AA0136 |  |  | 465d5717-b929-5a90-a4a8-47945b1b586e | ingest.documents.raw_extraction |
| service_center_details | {"fax": "263 1010", "email": "navjivanmotors@gmail.com", "phone_numbers": ["263 1000", "263 2000", "263 3000"], "organization_name": "Navjivan Motors Pvt. Ltd.", "organization_type": "Authorized Hyun… |  | {'fax': '263 1010', 'email': 'navjivanmotors@gmail.com', 'phone_numbers': ['263 1000', '263 2000', '263 3000'], 'organization_name': 'Navjivan Motors Pvt. Ltd.', 'organization_type': 'Authorized Hyun… | 1bbe2ce2-9359-5aa7-98f1-d21aa3b4746a | ingest.documents.raw_extraction |
| date_of_gate_pass_issuance | 09/08/2023 |  |  | cb95a01a-9cae-5d0c-ae14-d615bdb7c30d | ingest.documents.raw_extraction |
| serial_number_of_the_gate_pass | 1800 |  |  | fe047750-2680-549b-b408-b58b0e3f7d0f | ingest.documents.raw_extraction |
| time_of_vehicle_entry/check-in | 10:45 PM |  |  | 8454ee1b-0fa3-5c86-a262-fe7aa243629d | ingest.documents.raw_extraction |
| odometer_reading_in_kilometers_at_time_o | 219213 |  |  | 6c6911be-b180-5dbb-8e88-c874cb836b6f | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `219358654_Repair_Estimate` — `repair_estimate`  (row uuid `e653a616-1acb-4378-b9c9-3b7e92e15655`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| amount | 112712.22 |  |  | 0b038f4b-8c96-5d49-b177-a4b691295937 | ingest.documents.raw_extraction |
| totals | {"cgst_rate": null, "igst_rate": null, "sgst_rate": null, "total_tax": null, "cgst_amount": null, "grand_total": 112712.22, "igst_amount": null, "sgst_amount": null, "total_labor": 65099.42, "total_p… |  | {'cgst_rate': None, 'igst_rate': None, 'sgst_rate': None, 'total_tax': None, 'cgst_amount': None, 'grand_total': 112712.22, 'igst_amount': None, 'sgst_amount': None, 'total_labor': 65099.42, 'total_p… | 132ffb4a-6efa-5cc0-838c-ad668037facf | ingest.documents.raw_extraction |
| amount_2 | 47612.80 |  |  | b5486c6a-c357-57a7-93db-1be4716e316c | ingest.documents.raw_extraction |
| labor_list | [{"rate": 800.0, "hours": null, "total": 944.0, "tax_type": "inclusive_gst", "job_number": null, "description": "RADIATOR ASSY", "serial_number": 1, "operation_code": null}, {"rate": 560.0, "hours": … |  | [{'rate': 800.0, 'hours': None, 'total': 944.0, 'tax_type': 'inclusive_gst', 'job_number': None, 'description': 'RADIATOR ASSY', 'serial_number': 1, 'operation_code': None}, {'rate': 560.0, 'hours': … | 8fe14333-2166-5d49-8460-e9346c4581b7 | ingest.documents.raw_extraction |
| paint_list | [] |  | [] | 8e6ff94b-91a1-5565-ab56-965613d92be0 | ingest.documents.raw_extraction |
| parts_list | [{"total": 1024.03, "quantity": 1.0, "tax_type": "inclusive_gst", "part_type": "Other", "job_number": null, "unit_price": 867.82, "description": "310 ml-SEALANT KIT-W/S GLASS", "part_number": "08M988… |  | [{'total': 1024.03, 'quantity': 1.0, 'tax_type': 'inclusive_gst', 'part_type': 'Other', 'job_number': None, 'unit_price': 867.82, 'description': '310 ml-SEALANT KIT-W/S GLASS', 'part_number': '08M988… | 8a2558d3-1afd-52ff-8b63-27e11316d3c0 | ingest.documents.raw_extraction |
| person_name | MAHESHKUMAR INDRASING VASAVA |  |  | 3c479128-7c7d-59cc-944b-1ef7de5ba245 | ingest.documents.raw_extraction |
| claim_number | R202305933 |  |  | da35a6d3-5b3a-5edb-8dbb-d4cee880e790 | ingest.documents.raw_extraction |
| insurer_name | Bajaj Allianz General Insurance Company Limited |  |  | 02f9d008-e4b6-5842-8138-eac801ca1ccb | ingest.documents.raw_extraction |
| engine_number | G3HADM199755 |  |  | e10404df-a550-5495-a4ea-b792b110a7f5 | ingest.documents.raw_extraction |
| workshop_name | M/S NAVJIVAN MOTORS PVT.LTD. |  |  | fcde1f08-f462-5b6b-ae41-91fb4411d169 | ingest.documents.raw_extraction |
| chassis_number | MALA351ALDM226944 |  |  | 85620315-cf2a-5545-b402-8e43dba6c811 | ingest.documents.raw_extraction |
| vendor_details | {"vendor_cin": null, "vendor_pan": null, "vendor_name": "M/S NAVJIVAN MOTORS PVT.LTD.", "vendor_gstin": null, "vendor_address": null, "vendor_contact": null, "place_of_supply": null, "service_advisor… |  | {'vendor_cin': None, 'vendor_pan': None, 'vendor_name': 'M/S NAVJIVAN MOTORS PVT.LTD.', 'vendor_gstin': None, 'vendor_address': None, 'vendor_contact': None, 'place_of_supply': None, 'service_advisor… | 9831b8dd-6c0c-53e0-86f3-bb0807124a5b | ingest.documents.raw_extraction |
| vehicle_details | {"make": null, "color": "C.White", "model": "EON", "variant": null, "fuel_type": null, "date_of_sale": null, "engine_number": "G3HADM199755", "hypothecation": null, "chassis_number": "MALA351ALDM2269… |  | {'make': None, 'color': 'C.White', 'model': 'EON', 'variant': None, 'fuel_type': None, 'date_of_sale': None, 'engine_number': 'G3HADM199755', 'hypothecation': None, 'chassis_number': 'MALA351ALDM2269… | df4f449d-eb19-517a-9547-f997a542f2e1 | ingest.documents.raw_extraction |
| customer_details | {"customer_name": "MAHESHKUMAR INDRASING VASAVA", "customer_address": "6 NANA VARACHHA HOUSING SOC.DHAL NANA VARACHHA KAMREJ SURAT", "customer_contact": null} |  | {'customer_name': 'MAHESHKUMAR INDRASING VASAVA', 'customer_address': '6 NANA VARACHHA HOUSING SOC.DHAL NANA VARACHHA KAMREJ SURAT', 'customer_contact': None} | f48d953a-860c-5a4f-896b-e288eb0715e7 | ingest.documents.raw_extraction |
| insurance_linkage | {"claim_number": "R202305933", "policy_number": null, "surveyor_name": null, "insurance_company": "Bajaj Allianz General Insurance Company Limited", "authorization_number": null} |  | {'claim_number': 'R202305933', 'policy_number': None, 'surveyor_name': None, 'insurance_company': 'Bajaj Allianz General Insurance Company Limited', 'authorization_number': None} | 2de91c2b-bdd0-57e4-934a-5e30177a9e7a | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AA0736 |  |  | b50c1b67-d7bc-5b78-91ac-71a40ec1ea4c | ingest.documents.raw_extraction |
| repair_estimate_number | ET23080090 |  |  | e71dc912-d4d4-5208-bd52-026e499babd1 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `219430367_Pre_Inspection_Photographs_Reports` — `vehicle_document`  (row uuid `5daad72d-9ffa-48d3-8d54-ab627259ec12`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| amount | 1197 |  |  | 187d3635-72a9-5339-ab22-d269465e6d74 | ingest.documents.raw_extraction |
| issue_date | 2013-10-17 |  |  | 6d457fdb-2df6-5f55-acf0-ec71b78510db | ingest.documents.raw_extraction |
| expiry_date | 2028-10-16 |  |  | 5f42d811-82b3-549d-98b2-387d5cbb1f8a | ingest.documents.raw_extraction |
| engine_number | G3JH0M199756 |  |  | c7b6323b-12cc-5e06-8473-a8acae3c7e26 | ingest.documents.raw_extraction |
| chassis_number | MALA351AL0R226944 |  |  | 88bbfe1c-7017-51ec-8236-9d75c5334d2f | ingest.documents.raw_extraction |
| vehicle_details | {"make": "HYUNDAI", "color": "WHITE", "model": "i10 SPORT 2 BWM", "body_type": null, "fuel_type": "PETROL", "engine_number": "G3JH0M199756", "chassis_number": "MALA351AL0R226944", "registration_numbe… |  | {'make': 'HYUNDAI', 'color': 'WHITE', 'model': 'i10 SPORT 2 BWM', 'body_type': None, 'fuel_type': 'PETROL', 'engine_number': 'G3JH0M199756', 'chassis_number': 'MALA351AL0R226944', 'registration_numbe… | b45318d2-c0f8-5fca-8587-5b2b11629411 | ingest.documents.raw_extraction |
| organization_name | HYUNDAI |  |  | 8a09c1e0-7219-53a9-8841-59ccc0a16c95 | ingest.documents.raw_extraction |
| organization_name_2 | Government of Gujarat |  |  | a8fe30df-66c1-5906-b98f-e3fc87e4215b | ingest.documents.raw_extraction |
| registration_details | {"issue_date": "2013-10-17", "validity_date": "2028-10-16", "vehicle_class": "LMV (CAR)", "issuing_authority": "Government of Gujarat", "hypothecation_status": "NIL", "issue_date_original_script": "1… |  | {'issue_date': '2013-10-17', 'validity_date': '2028-10-16', 'vehicle_class': 'LMV (CAR)', 'issuing_authority': 'Government of Gujarat', 'hypothecation_status': 'NIL', 'issue_date_original_script': '1… | ced8ffe6-5d6f-5997-92a3-6a0346d12578 | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AA0736 |  |  | 786969f6-cc4d-55d7-a68d-681539a78d32 | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "Vehicle Details", "field_label": "Vehicle Color", "field_value": "WHITE", "field_label_original_script": "Color", "field_value_original_script": "WHITE"}, {"section": "Vehicle Details",… |  | [{'section': 'Vehicle Details', 'field_label': 'Vehicle Color', 'field_value': 'WHITE', 'field_label_original_script': 'Color', 'field_value_original_script': 'WHITE'}, {'section': 'Vehicle Details',… | 50b3e6b5-3bfe-5738-9b19-b4290ffe4633 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `222633146_Statement_of_Insured` — `insured_statement`  (row uuid `0c0a6982-7c61-4644-bfa4-2c99d0d4db57`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| person_name | Prasann Maheshwari |  |  | f8eb2cbf-77a3-509a-89d6-869fee95bb96 | ingest.documents.raw_extraction |
| phone_number | 9411411 |  |  | e36f046f-8e44-55f2-855b-a6820d59eafb | ingest.documents.raw_extraction |
| statement_date | 19/09/2023 |  |  | d7a4eeb6-3459-5c6f-9d1e-b5261140dd24 | ingest.documents.raw_extraction |
| statement_details | {"age": null, "id_no": null, "s_w_o": null, "state": null, "tehsil": null, "country": "India", "district": null, "signature": "[PRESENT - handwritten signature visible at bottom of document]", "claim… |  | {'age': None, 'id_no': None, 's_w_o': None, 'state': None, 'tehsil': None, 'country': 'India', 'district': None, 'signature': '[PRESENT - handwritten signature visible at bottom of document]', 'claim… | 320cba5f-55f5-5ae5-9040-d3717a4fa833 | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "signature_block", "field_label": "Document Author/Signatory", "field_value": "Prasann Maheshwari", "field_label_original_script": null, "field_value_original_script": null}, {"section":… |  | [{'section': 'signature_block', 'field_label': 'Document Author/Signatory', 'field_value': 'Prasann Maheshwari', 'field_label_original_script': None, 'field_value_original_script': None}, {'section':… | 0b4ec0ef-d9ba-56b4-bf52-938f635dc79c | ingest.documents.raw_extraction |
| reference_number_or_identifier | 9474625160 |  |  | 06fa02ae-94ed-5030-ae26-1ad745469312 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json
{
  "statement_details": {
    "age": null,
    "id_no": null,
    "s_w_o": null,
    "state": null,
    "tehsil": null,
    "country": "India",
    "district": null,
    "signature": "[PRESENT - handwritten signature visible at bottom of document]",
    "claim_number": null,
    "full_address": "[HANDWRITTEN: Gujarati address - requires verification]",
    "insured_name": null,
    "phone_number": 9411411,
    "policy_number": null,
    "police_station": null,
    "statement_date": "2023-09-19",
    "contact_information": "9411411 [PARTIAL]",
    "incident_description": "[HANDWRITTEN: Gujarati narrative - detailed transcription requires native script verification]",
    "accident_admitted_or_denied": null
  }
}
```

### Doc `222633187_Statement_of_Driver` — `driver_statement`  (row uuid `dabf5699-218e-48d4-992e-a7594c785bf6`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| driver_name | [Gujarati text - name not clearly legible] |  |  | 5f0e9b00-4075-5536-836b-ee175adbf2d0 | ingest.documents.raw_extraction |
| phone_number | 8308953545 |  |  | 523a30dd-0e52-5ecc-b0ce-9d03640ca963 | ingest.documents.raw_extraction |
| statement_details | {"address": null, "witnesses": null, "driver_name": null, "incident_date": "2023-08-19", "contact_number": "8308953545", "license_number": null, "vehicle_details": null, "date_of_accident": "2023-08-… |  | {'address': None, 'witnesses': None, 'driver_name': None, 'incident_date': '2023-08-19', 'contact_number': '8308953545', 'license_number': None, 'vehicle_details': None, 'date_of_accident': '2023-08-… | 4fb7ef04-aa4c-5dc1-ac2a-ef586101a04e | ingest.documents.raw_extraction |
| incident/accident_date | 19-08-2023 |  |  | 1f31f434-2524-5c78-889c-b0a33cb25143 | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "Header", "field_label": "Date", "field_value": "19-08-2023", "field_label_original_script": null, "field_value_original_script": "19\|08\|2023"}, {"section": "Header", "field_label": "M… |  | [{'section': 'Header', 'field_label': 'Date', 'field_value': '19-08-2023', 'field_label_original_script': None, 'field_value_original_script': '19\|08\|2023'}, {'section': 'Header', 'field_label': 'M… | 77aa8e68-3bb8-5444-bbbf-723e2f8550b7 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json
{
  "statement_details": {
    "address": null,
    "witnesses": null,
    "driver_name": null,
    "incident_date": "2023-08-19",
    "contact_number": "8308953545",
    "license_number": null,
    "vehicle_details": null,
    "date_of_accident": "2023-08-19",
    "driver_signature": "[PRESENT - handwritten signature/mark visible at bottom of page 2]",
    "dl_no_confirmation": null,
    "incident_description": "[HANDWRITTEN GUJARATI TEXT - Full narrative present but not transliterated to avoid hallucination. Approximately 400-600 words describing incident details in Gujarati script.]",
    "accident_admitted_denied": null,
    "no_of_members_injured_died": null
  }
}
```

### Doc `222633313_Vehicle_Damage_Photo` — `photograph`  (row uuid `aa3ca302-8ecc-4bfc-acf7-9a24b12ed44c`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| location | Gujarat |  |  | a6972268-e784-5983-b64c-f7f18b08614e | ingest.documents.raw_extraction |
| document_id | GJ27AA0736 |  |  | bad749ef-5656-57a8-84af-804bca0de746 | ingest.documents.raw_extraction |
| vehicle_details | {"make": "Hyundai", "color": "White", "model": "i10", "body_type": "Hatchback", "damage_type": "Front-end collision damage", "damage_severity": "Severe", "damage_description": "Hood severely crushed … |  | {'make': 'Hyundai', 'color': 'White', 'model': 'i10', 'body_type': 'Hatchback', 'damage_type': 'Front-end collision damage', 'damage_severity': 'Severe', 'damage_description': 'Hood severely crushed … | 8e2dcfd9-6163-5cb4-9a33-5621526aa309 | ingest.documents.raw_extraction |
| damage_assessment | {"damage_extent": "Severe front-end collision with hood crushed, headlights damaged, bumper affected", "marking_observed": "Red tape X-pattern across hood (likely damage marking or repair indication)… |  | {'damage_extent': 'Severe front-end collision with hood crushed, headlights damaged, bumper affected', 'marking_observed': 'Red tape X-pattern across hood (likely damage marking or repair indication)… | 712d0d1c-e04d-5596-ac2d-5a9403d13244 | ingest.documents.raw_extraction |
| organization_name | Hyundai i10 |  |  | 4b25eb38-fec7-59f7-b330-e18d1289339d | ingest.documents.raw_extraction |
| photograph_metadata | {"location": "Parking lot with multiple vehicles and buildings visible", "visible_persons": "Persons in blue clothing and checkered shirt visible in some frames", "photograph_angles": ["Side view (Pa… |  | {'location': 'Parking lot with multiple vehicles and buildings visible', 'visible_persons': 'Persons in blue clothing and checkered shirt visible in some frames', 'photograph_angles': ['Side view (Pa… | ba538023-79f8-56bb-b12d-86852fdffdd4 | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AA0736 |  |  | 00d6a426-e088-5b9d-b94f-f3984c19692d | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "Vehicle Identification", "field_label": "Vehicle Color", "field_value": "White"}, {"section": "Damage Assessment", "field_label": "Damage Marking", "field_value": "Red tape X-pattern ac… |  | [{'section': 'Vehicle Identification', 'field_label': 'Vehicle Color', 'field_value': 'White'}, {'section': 'Damage Assessment', 'field_label': 'Damage Marking', 'field_value': 'Red tape X-pattern ac… | 4d863c29-21e9-52f0-8d81-9c50355a2c27 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `222633407_Spot_Photo_Sketch` — `photograph`  (row uuid `b24a6a1d-7def-49b2-b19f-c24ed87bdef7`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| location | Surat |  |  | 51a731c2-0c47-5921-b7ed-3286afbe8031 | ingest.documents.raw_extraction |
| location_2 | India |  |  | 5411a0c9-b60c-51b1-b1d4-b72057e54ac4 | ingest.documents.raw_extraction |
| organization_name | Unacademy |  |  | 203a4adf-7bf4-546a-8510-46cea9479e3d | ingest.documents.raw_extraction |
| photograph_details | {"image_types": ["Street scene with commercial activity", "Empty residential street", "Street scene with pedestrian", "Street scene with pedestrian in traditional attire", "Residential area street", … |  | {'image_types': ['Street scene with commercial activity', 'Empty residential street', 'Street scene with pedestrian', 'Street scene with pedestrian in traditional attire', 'Residential area street', … | 814d97c0-d4f2-5497-9265-64a2df16d2e7 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `222633435_Any_Other` — `other`  (row uuid `d72d1318-419f-4d3b-990d-3c57c9854458`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| amount | 1510664 |  |  | 79e869fa-a369-5f53-99a6-4775834adf97 | ingest.documents.raw_extraction |
| amount_2 | 29950 |  |  | 8e529827-09bd-5efe-827e-907c46a0740c | ingest.documents.raw_extraction |
| amount_3 | 1510652 |  |  | e06f85a7-8c5d-5a73-b79c-a4d40754d09a | ingest.documents.raw_extraction |
| amount_4 | 149000 |  |  | 50b2ea3f-6af7-5258-9e09-2ba1e337e573 | ingest.documents.raw_extraction |
| location | Candu Uka |  |  | 6ce4e804-599f-5cfc-9e8b-f7d3b2343287 | ingest.documents.raw_extraction |
| person_name | Prakash Chaudhari |  |  | d89ebad8-d87f-586c-aae3-b7c6b2eeae9f | ingest.documents.raw_extraction |
| photographs | {"photo_1": "Person in checkered shirt and glasses writing on document at table", "photo_2": "Vehicle photograph labeled 'Candu Uka' dated August 3, 3:47 PM showing commercial/taxi vehicle", "photo_3… |  | {'photo_1': 'Person in checkered shirt and glasses writing on document at table', 'photo_2': "Vehicle photograph labeled 'Candu Uka' dated August 3, 3:47 PM showing commercial/taxi vehicle", 'photo_3… | d3fdba7b-dbc8-535e-825f-70e837fec96b | ingest.documents.raw_extraction |
| phone_number | 90793 85368 |  |  | 42346f7b-d5b3-5e84-93b2-757aa5085e1a | ingest.documents.raw_extraction |
| person_name_2 | Mahesh Vasava |  |  | 3780c361-59a9-5d12-8bdb-d5d98ade123c | ingest.documents.raw_extraction |
| phone_number_2 | 99133 16746 |  |  | 20ab0030-80ac-5615-a5d1-96ad7bfdefb4 | ingest.documents.raw_extraction |
| digital_records | {"google_accounts_accessed": [{"email": "uahachaudhari28@gmail.com", "account_name": "Prakash Chaudhari"}, {"email": "mivasava1988@gmail.com", "account_name": "Mahesh Vasava"}], "specific_date_highli… |  | {'google_accounts_accessed': [{'email': 'uahachaudhari28@gmail.com', 'account_name': 'Prakash Chaudhari'}, {'email': 'mivasava1988@gmail.com', 'account_name': 'Mahesh Vasava'}], 'specific_date_highli… | 968fe606-e8ca-5561-afcc-b57d78e05f86 | ingest.documents.raw_extraction |
| vehicle_details | {"model_year": "2011", "odometer_reading": "500012/01", "registration_number": "9227463964", "odometer_reading_original_script": "500012/01", "registration_number_original_script": "9227463964"} |  | {'model_year': '2011', 'odometer_reading': '500012/01', 'registration_number': '9227463964', 'odometer_reading_original_script': '500012/01', 'registration_number_original_script': '9227463964'} | edf79e0c-9c0b-5802-ac76-5d4a0f818b3b | ingest.documents.raw_extraction |
| odometer_reading | 500012/01 |  |  | a82e6ac2-5f51-5127-8269-c6e97eceb9d7 | ingest.documents.raw_extraction |
| organization_name | Bupusiraum Cabs |  |  | ad3f340a-7c34-572c-93a2-85694fdbecf1 | ingest.documents.raw_extraction |
| data_quality_notes | {"language_barrier": "Significant portions of form are in Gujarati script; English translation/verification required for complete accuracy", "document_completeness": "Form appears incomplete with sig… |  | {'language_barrier': 'Significant portions of form are in Gujarati script; English translation/verification required for complete accuracy', 'document_completeness': 'Form appears incomplete with sig… | c44238e5-f50b-5cf3-ba5c-e023ead39d37 | ingest.documents.raw_extraction |
| dealership_details | {"tagline": "Drive your dreams", "location": "Urban area with multiple vehicles in lot", "contact_numbers": ["90793 85368", "99133 16746"], "dealership_name": "Bupusiraum Cabs", "dealership_name_orig… |  | {'tagline': 'Drive your dreams', 'location': 'Urban area with multiple vehicles in lot', 'contact_numbers': ['90793 85368', '99133 16746'], 'dealership_name': 'Bupusiraum Cabs', 'dealership_name_orig… | ef94d58b-ae4c-519f-931b-f7ed74ff522d | ingest.documents.raw_extraction |
| vehicle_model_year | 2011 |  |  | ff3eaabd-1ab7-5fd1-99b6-9fb365b10330 | ingest.documents.raw_extraction |
| vehicle_registration | 9227463964 |  |  | 483da377-4754-5d23-a214-6de83e085427 | ingest.documents.raw_extraction |
| purchase_form_details | {"form_date": "27/07/2023", "form_status": "Partially filled with handwritten entries", "form_date_iso": "2023-07-27", "form_language": "Gujarati with English headers", "financial_breakdown": {"badi"… |  | {'form_date': '27/07/2023', 'form_status': 'Partially filled with handwritten entries', 'form_date_iso': '2023-07-27', 'form_language': 'Gujarati with English headers', 'financial_breakdown': {'badi'… | f0591228-62d3-5a0e-ac89-4ff39ca3efad | ingest.documents.raw_extraction |
| vehicle_registration_2 | 9455504 |  |  | f7aa5b21-44a6-5c5f-b03b-73b0574b2c16 | ingest.documents.raw_extraction |
| date_on_vehicle_purchase_form | 27/07/2023 |  |  | 258bbbc1-3e42-5dae-9a6f-9388da182ebb | ingest.documents.raw_extraction |
| email_address_of_mahesh_vasava | mivasava1988@gmail.com |  |  | 1562109d-0668-5b60-816e-2c0ec6308f40 | ingest.documents.raw_extraction |
| email_address_of_prakash_chaudhari | uahachaudhari28@gmail.com |  |  | 8092259a-efdc-5741-bddb-23e852334387 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `222696526_Statement_of_Insured` — `insured_statement`  (row uuid `efac8d30-f46f-4eb0-9d11-437c83c2fb8b`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| person_name | Mahesh Jyear |  |  | cfb7bb4c-57aa-59a3-ae71-893a5d7ea384 | ingest.documents.raw_extraction |
| insured_name | [HANDWRITTEN: Illegible - appears to be insured's name] |  |  | 3d485a9a-2210-5c14-a899-fe2fa583fe27 | ingest.documents.raw_extraction |
| phone_number | 9227637160 |  |  | 84beac75-9e61-579e-882c-50bb1e5a6ac7 | ingest.documents.raw_extraction |
| person_name_2 | [HANDWRITTEN: Mahesh Anjania or similar] |  |  | b84b228b-e7e7-502e-8185-ca2d7a9e9af5 | ingest.documents.raw_extraction |
| statement_details | {"age": null, "id_no": null, "s_w_o": null, "state": "[HANDWRITTEN: State name in Gujarati - illegible]", "tehsil": "[HANDWRITTEN: Tehsil name in Gujarati - illegible]", "country": "\u0aad\u0abe\u0ab… |  | {'age': None, 'id_no': None, 's_w_o': None, 'state': '[HANDWRITTEN: State name in Gujarati - illegible]', 'tehsil': '[HANDWRITTEN: Tehsil name in Gujarati - illegible]', 'country': 'ભારત (India)', 'd… | 33baba70-e4a4-554c-a849-d9597748a36a | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "administrative", "field_label": "RCT", "field_value": "Mahesh Jyear", "field_label_original_script": null, "field_value_original_script": null}, {"section": "administrative", "field_lab… |  | [{'section': 'administrative', 'field_label': 'RCT', 'field_value': 'Mahesh Jyear', 'field_label_original_script': None, 'field_value_original_script': None}, {'section': 'administrative', 'field_lab… | 25f8e86f-af5d-51e8-922d-b933b929ee76 | ingest.documents.raw_extraction |
| printed_reference/case_number_on_documen | OC-24-2203-1801-00002660 |  |  | 23d9b964-fb82-5dd1-a873-588913a5f6ea | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json
{
  "statement_details": {
    "age": null,
    "id_no": null,
    "s_w_o": null,
    "state": "[HANDWRITTEN: State name in Gujarati - illegible]",
    "tehsil": "[HANDWRITTEN: Tehsil name in Gujarati - illegible]",
    "country": "\u0aad\u0abe\u0ab0\u0aa4 (India)",
    "district": "[HANDWRITTEN: District name in Gujarati - illegible]",
    "signature": "[HANDWRITTEN: Signature present at bottom of document]",
    "claim_number": null,
    "full_address": "[HANDWRITTEN: Address details in Gujarati - partially legible]",
    "insured_name": null,
    "phone_number": 9227637160,
    "policy_number": null,
    "police_station": "[HANDWRITTEN: Police station name in Gujarati - illegible]",
    "statement_date": null,
    "contact_information": null,
    "incident_description": "[HANDWRITTEN: Gujarati narrative describing accident/incident circumstances - full text illegible due to handwriting quality and script complexity]",
    "accident_admitted_or_denied": null
  }
}
```

### Doc `223214762_Investigation_Report` — `correspondence`  (row uuid `5412926d-545c-40a3-a95e-08fe63391f61`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| qc_flags | {"pmr_procured": null, "death_or_injury": false, "chargesheet_filed": null, "driver_implant_flag": "Y", "driver_injury_provided": false, "police_report_procured": null, "treatment_paper_procured": nu… |  | {'pmr_procured': None, 'death_or_injury': False, 'chargesheet_filed': None, 'driver_implant_flag': 'Y', 'driver_injury_provided': False, 'police_report_procured': None, 'treatment_paper_procured': No… | d3a291eb-5bde-59d7-8469-2e3f455d6673 | ingest.documents.raw_extraction |
| dl_number | GJ05/028137/06 |  |  | a254c8b3-601d-5d72-8eaf-b627f5291607 | ingest.documents.raw_extraction |
| pan_number | BOTPV1128N |  |  | d30dd126-4aab-5cf4-8656-fa303d616671 | ingest.documents.raw_extraction |
| driver_name | Prakashbhai Chaudhari |  |  | a0fee6dc-a6e9-59d9-a046-506ed2da8673 | ingest.documents.raw_extraction |
| person_name | Abhishek Gaur |  |  | 33dc536e-adc6-5f4a-b532-f6299ef140cd | ingest.documents.raw_extraction |
| report_date | 2023-09-18 |  |  | e0a0e9bc-5da6-5426-bafd-cddc16de9526 | ingest.documents.raw_extraction |
| report_time | 02:57:46 PM |  |  | bb53a42d-d311-566b-af16-1f87e95e5726 | ingest.documents.raw_extraction |
| claim_number | OC-24-2203-1801-00002660 |  |  | f1fc68c5-b192-5b09-bc79-f09fa212155d | ingest.documents.raw_extraction |
| insured_name | Maheshkumar Vasava |  |  | 64baded4-5bad-5979-800f-61e69670f0fb | ingest.documents.raw_extraction |
| phone_number | 9773228144 |  |  | 26c97d80-c093-5fc3-ab92-dd9cc03d0ef5 | ingest.documents.raw_extraction |
| claim_details | {"claim_number": "OC-24-2203-1801-00002660", "date_of_loss": "2023-08-08", "product_name": "Private Car - Package Policy", "policy_number": "OG-24-2203-1801-00005412", "referral_days": 9, "intimation… |  | {'claim_number': 'OC-24-2203-1801-00002660', 'date_of_loss': '2023-08-08', 'product_name': 'Private Car - Package Policy', 'policy_number': 'OG-24-2203-1801-00005412', 'referral_days': 9, 'intimation… | e400b380-1a48-5c23-bb3c-6cc0a1a727fc | ingest.documents.raw_extraction |
| crime_details | {"fir_filed": false, "fir_number": null, "ipc_sections": null, "mv_act_sections": null, "type_of_complaint": "No Complaint", "police_station_name": null} |  | {'fir_filed': False, 'fir_number': None, 'ipc_sections': None, 'mv_act_sections': None, 'type_of_complaint': 'No Complaint', 'police_station_name': None} | 66c108ca-f0d8-5fc1-8bc9-4eb28325607d | ingest.documents.raw_extraction |
| employer_name | Radhi Lab |  |  | cafaa179-c204-502c-969c-17e342965000 | ingest.documents.raw_extraction |
| engine_number | G3HADM199 |  |  | f699d483-d482-5432-b81c-ac8cb5803645 | ingest.documents.raw_extraction |
| policy_number | OG-24-2203-1801-00005412 |  |  | 449481ae-120d-54ea-b358-8077108e10d3 | ingest.documents.raw_extraction |
| workshop_name | Navjivan Hyundai Garage |  |  | 8d31b582-b293-5687-925a-9a0d9c86d743 | ingest.documents.raw_extraction |
| chassis_number | MALA351ALDM226944 |  |  | 5069e4f6-4d24-5c6f-91ca-ada1df61d9d2 | ingest.documents.raw_extraction |
| driver_details | {"driver_name": "PRAKASHBHAI CHAUDHARI", "dl_validity_to": "2026-04-11", "driver_address": "B M COMPLEX, NANA VARACHHA, SURAT", "dl_validity_from": "2006-04-12", "driver_contact_number": "8306895545"… |  | {'driver_name': 'PRAKASHBHAI CHAUDHARI', 'dl_validity_to': '2026-04-11', 'driver_address': 'B M COMPLEX, NANA VARACHHA, SURAT', 'dl_validity_from': '2006-04-12', 'driver_contact_number': '8306895545'… | c81afe29-c322-537c-8f29-2c42495ba4b4 | ingest.documents.raw_extraction |
| garage_details | {"garage_name": "Navjivan Hyundai Garage", "garage_state": "GUJARAT", "job_card_date": "2023-08-09", "network_status": "Non-Network Garage", "garage_district": "SURAT", "garage_pin_code": "394210", "… |  | {'garage_name': 'Navjivan Hyundai Garage', 'garage_state': 'GUJARAT', 'job_card_date': '2023-08-09', 'network_status': 'Non-Network Garage', 'garage_district': 'SURAT', 'garage_pin_code': '394210', '… | fda88858-e4cd-59ca-b9b8-93c90186aff5 | ingest.documents.raw_extraction |
| phone_number_2 | 8306895545 |  |  | ddf770a6-d76d-5b18-826d-46f8d25fd3cc | ingest.documents.raw_extraction |
| towing_details | {"towing_done": false, "towing_company_name": null, "towing_company_address": null} |  | {'towing_done': False, 'towing_company_name': None, 'towing_company_address': None} | 290ff675-0305-5bc4-9436-fa5eafd5808e | ingest.documents.raw_extraction |
| insured_details | {"state": "GUJARAT", "district": "SURAT", "pin_code": "395006", "last_name": "VASAVA", "first_name": "MAHESHKUMAR", "occupation": "Pvt. Service", "middle_name": "INDRASING", "date_of_birth": "1988-09… |  | {'state': 'GUJARAT', 'district': 'SURAT', 'pin_code': '395006', 'last_name': 'VASAVA', 'first_name': 'MAHESHKUMAR', 'occupation': 'Pvt. Service', 'middle_name': 'INDRASING', 'date_of_birth': '1988-09… | f970411b-1af7-572f-a4d3-a81d19c6b1e6 | ingest.documents.raw_extraction |
| vehicle_details | {"make": "HYUNDAI", "model": "EON", "hypothecated": true, "owner_serial": 2, "engine_number": "G3HADM199", "chassis_number": "MALA351ALDM226944", "class_of_vehicle": "Private Car", "registration_date… |  | {'make': 'HYUNDAI', 'model': 'EON', 'hypothecated': True, 'owner_serial': 2, 'engine_number': 'G3HADM199', 'chassis_number': 'MALA351ALDM226944', 'class_of_vehicle': 'Private Car', 'registration_date… | fb180e25-bc3a-5cac-a087-826c640a91da | ingest.documents.raw_extraction |
| accident_details | {"injuries": "No injuries reported", "accident_date": "2023-08-08", "accident_time": "21:15", "damage_location": "Front side of vehicle", "accident_location": "Nana Varachha, Surat", "photographs_tak… |  | {'injuries': 'No injuries reported', 'accident_date': '2023-08-08', 'accident_time': '21:15', 'damage_location': 'Front side of vehicle', 'accident_location': 'Nana Varachha, Surat', 'photographs_tak… | 67038433-1c1b-5a9b-91aa-4baa13d1804c | ingest.documents.raw_extraction |
| incident_location | Nana Varachha, Surat |  |  | fb54b9d1-a063-50fb-8e1d-e7040e6a8561 | ingest.documents.raw_extraction |
| organization_name | Bappa Sitaram Car Mela |  |  | 58546879-4ba3-5e22-99fb-6962eb489736 | ingest.documents.raw_extraction |
| report_printed_by | abhishek.gaur01@bajajallianz.co.in |  |  | 38f55227-8be2-5b84-8874-cc7570ff23b3 | ingest.documents.raw_extraction |
| incident_location_2 | Moti Nagar Society |  |  | 9ab05a69-002a-532f-8fb1-935fb1a9fa5e | ingest.documents.raw_extraction |
| organization_name_2 | Bajaj Finance |  |  | 1db58b3e-8c2f-5f4b-abcd-f030968a543c | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AA0736 |  |  | 21f09fb5-1872-5b63-adcb-19f9c6011a0e | ingest.documents.raw_extraction |
| investigation_findings | {"key_finding": "Driver was changed in the case. Insured (Maheshkumar Vasava) was actually driving the vehicle, not his friend Prakashbhai Chaudhari as initially stated.", "claim_status": "Withdrawn … |  | {'key_finding': 'Driver was changed in the case. Insured (Maheshkumar Vasava) was actually driving the vehicle, not his friend Prakashbhai Chaudhari as initially stated.', 'claim_status': 'Withdrawn … | 5f693ce6-c8ae-5ec7-9195-277a70749a1e | ingest.documents.raw_extraction |
| pin_code_of_garage_address | 394210 |  |  | 668d4e57-70a1-539a-b177-3ee719fa8d35 | ingest.documents.raw_extraction |
| pin_code_of_insured's_address | 395006 |  |  | d82d4e43-efcf-5bbf-8331-d0a9200450df | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `223215102_Investigation_Report` — `correspondence`  (row uuid `0ed4a2c3-1f68-4667-9090-f5abd921d8a9`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| dl_number | GJ05/028137/06 |  |  | 0971b3e9-3bd5-5ef6-b5ef-9ee98e34fc7f | ingest.documents.raw_extraction |
| pan_number | BOTPV1128N |  |  | f21828e7-2f93-57c3-a84e-4702ee0ddba8 | ingest.documents.raw_extraction |
| claim_number | OC-24-2203-1801-00002660 |  |  | d87f94a5-42d6-5c50-bf9b-88ab681c99a2 | ingest.documents.raw_extraction |
| insured_name | Maheshkumar Indrasing Vasava |  |  | efc7d9c4-675e-5cdf-912c-2977c0a08394 | ingest.documents.raw_extraction |
| phone_number | 9773228144 |  |  | e8c083aa-9d5e-5e29-be20-6939d4a80bab | ingest.documents.raw_extraction |
| claim_details | {"claim_number": "OC-24-2203-1801-00002660", "date_of_loss": "2023-08-08", "product_name": "Private Car - Package Policy", "policy_number": "OG-24-2203-1801-00005412", "referral_days": 9, "intimation… |  | {'claim_number': 'OC-24-2203-1801-00002660', 'date_of_loss': '2023-08-08', 'product_name': 'Private Car - Package Policy', 'policy_number': 'OG-24-2203-1801-00005412', 'referral_days': 9, 'intimation… | 64e45581-57d4-5b7f-afaa-0e5036ff8b15 | ingest.documents.raw_extraction |
| crime_details | {"fir_filed": false, "fir_number": null, "accused_details": null, "type_of_complaint": "No Complaint", "police_station_name": null} |  | {'fir_filed': False, 'fir_number': None, 'accused_details': None, 'type_of_complaint': 'No Complaint', 'police_station_name': None} | dd8bb5bc-1aa1-570a-b798-c9b4d78bcb10 | ingest.documents.raw_extraction |
| employer_name | Radhi Lab |  |  | 481b163b-7728-5bcb-9d85-df2e1c4db92d | ingest.documents.raw_extraction |
| engine_number | G3HADM199 |  |  | e1881bbc-912e-5c3d-b62b-d2c55aa70df2 | ingest.documents.raw_extraction |
| policy_number | OG-24-2203-1801-00005412 |  |  | 2e285ee7-8ee2-547c-9099-49a11b8ce00c | ingest.documents.raw_extraction |
| workshop_name | Navjivan Hyundai Garage |  |  | a20c7122-359f-5fa8-b03a-cafbe1f9dc50 | ingest.documents.raw_extraction |
| chassis_number | MALA351ALDM226944 |  |  | 735b98bb-9212-5c81-9e4a-e24a520c3364 | ingest.documents.raw_extraction |
| driver_details | {"driver_name": "PRAKASHBHAI CHAUDHARI", "driver_address": "B M COMPLEX, NANA VARACHHA, SURAT", "address_visit_done": true, "authorized_to_drive": "LMV N/T", "dl_validity_to_date": "2026-04-11", "dri… |  | {'driver_name': 'PRAKASHBHAI CHAUDHARI', 'driver_address': 'B M COMPLEX, NANA VARACHHA, SURAT', 'address_visit_done': True, 'authorized_to_drive': 'LMV N/T', 'dl_validity_to_date': '2026-04-11', 'dri… | 9936a4c0-c8c8-5b3e-8ae9-a36fae048379 | ingest.documents.raw_extraction |
| garage_details | {"garage_pin": "394210", "garage_name": "Navjivan Hyundai Garage", "garage_state": "GUJARAT", "job_card_date": "2023-08-09", "network_garage": false, "garage_district": "SURAT", "garage_po_village": … |  | {'garage_pin': '394210', 'garage_name': 'Navjivan Hyundai Garage', 'garage_state': 'GUJARAT', 'job_card_date': '2023-08-09', 'network_garage': False, 'garage_district': 'SURAT', 'garage_po_village': … | 18708e92-9615-578b-a6d4-61805379d0b0 | ingest.documents.raw_extraction |
| insured_name_2 | Prakashbhai Chaudhari |  |  | 008a86f5-43f5-57cc-9476-bbcba71abe80 | ingest.documents.raw_extraction |
| phone_number_2 | 8306895545 |  |  | c6827afd-1a86-5cf9-8fe0-96634f2b7619 | ingest.documents.raw_extraction |
| insured_details | {"state": "GUJARAT", "district": "SURAT", "pin_code": "395006", "last_name": "VASAVA", "first_name": "MAHESHKUMAR", "occupation": "Pvt. Service", "middle_name": "INDRASING", "date_of_birth": "1988-09… |  | {'state': 'GUJARAT', 'district': 'SURAT', 'pin_code': '395006', 'last_name': 'VASAVA', 'first_name': 'MAHESHKUMAR', 'occupation': 'Pvt. Service', 'middle_name': 'INDRASING', 'date_of_birth': '1988-09… | f50918c9-dcc5-5ca8-ba2c-5588e09378c7 | ingest.documents.raw_extraction |
| vehicle_details | {"make": "HYUNDAI", "model": "EON", "hypothecated": true, "owner_serial": 2, "engine_number": "G3HADM199", "purchase_date": "2023-08-03", "purchase_time": "14:30", "chassis_number": "MALA351ALDM22694… |  | {'make': 'HYUNDAI', 'model': 'EON', 'hypothecated': True, 'owner_serial': 2, 'engine_number': 'G3HADM199', 'purchase_date': '2023-08-03', 'purchase_time': '14:30', 'chassis_number': 'MALA351ALDM22694… | 9c834d5b-2a79-52ee-8ecc-30cef3c35357 | ingest.documents.raw_extraction |
| accident_details | {"injuries": "No one was injured", "accident_date": "2023-08-08", "accident_time": "21:00 to 21:15", "accident_location": "Nana Varachha, Surat, in front of Motinagar", "photographs_taken": false, "t… |  | {'injuries': 'No one was injured', 'accident_date': '2023-08-08', 'accident_time': '21:00 to 21:15', 'accident_location': 'Nana Varachha, Surat, in front of Motinagar', 'photographs_taken': False, 't… | bede577e-d0fa-571d-95f5-bccc822ba538 | ingest.documents.raw_extraction |
| fraud_indicators | {"driver_implant": true, "gps_tracking_anomalies": true, "false_information_provided": true, "no_supporting_documentation": true, "driving_without_valid_license": true, "claim_withdrawn_after_investi… |  | {'driver_implant': True, 'gps_tracking_anomalies': True, 'false_information_provided': True, 'no_supporting_documentation': True, 'driving_without_valid_license': True, 'claim_withdrawn_after_investi… | b70bdc37-49d8-5304-baa7-0013e2bca3b7 | ingest.documents.raw_extraction |
| incident_location | Nana Varachha, Surat |  |  | 26ea46fc-b9b3-55a8-8dbe-036a1da278a3 | ingest.documents.raw_extraction |
| organization_name | Bappa Sitaram Car Mela |  |  | 9a076daf-aac2-5c04-b199-0182d8abcd1f | ingest.documents.raw_extraction |
| incident_location_2 | Moti Nagar Society |  |  | 9139824f-45d4-5ade-a794-76ef921af652 | ingest.documents.raw_extraction |
| incident_location_3 | Surat |  |  | 0d7f0f9e-40b5-5c33-aca2-5aa071268458 | ingest.documents.raw_extraction |
| incident_location_4 | Gujarat |  |  | caf77add-42b8-51a9-a3ec-be40aed584cc | ingest.documents.raw_extraction |
| organization_name_2 | Bajaj Finance |  |  | 0c7cc7b9-9a84-56bb-b6ac-eeff20431064 | ingest.documents.raw_extraction |
| investigation_status | Completed - Claim Withdrawn |  |  | 3be9cd86-b7c0-5e8c-b00d-40a31053f3fa | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AA0736 |  |  | 0252b49b-2c3c-5625-9c7a-a6c4e6871530 | ingest.documents.raw_extraction |
| investigation_findings | {"key_findings": ["Driver implant detected - stated driver was not actual driver", "Insured was driving without valid MDL", "Insured provided friend's driving license details", "No eyewitness confirm… |  | {'key_findings': ['Driver implant detected - stated driver was not actual driver', 'Insured was driving without valid MDL', "Insured provided friend's driving license details", 'No eyewitness confirm… | 1e753dd5-549e-5eb2-88c7-7517daa3f733 | ingest.documents.raw_extraction |
| accident_spot_verification | {"spot_landmark": "Moti Nagar Society", "eyewitness_available": false, "spot_location_address": "Nana Varachha, Surat", "cctv_cameras_available": false, "nearby_shops_confirmed_driver": false, "spot_… |  | {'spot_landmark': 'Moti Nagar Society', 'eyewitness_available': False, 'spot_location_address': 'Nana Varachha, Surat', 'cctv_cameras_available': False, 'nearby_shops_confirmed_driver': False, 'spot_… | ec36d735-14fb-58e3-8974-2bc65a5044dc | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `223233211_Supplier_Bill` — `repair_estimate`  (row uuid `ba1fdf22-196b-4f42-9518-054a3f8c757e`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| date | 2023-09-18 |  |  | 0f57da99-3ba5-58a3-b632-1ec83b1d04fa | ingest.documents.raw_extraction |
| gstin | 24AJAPD2623K12N |  |  | b4e48232-8a37-503b-9543-22a263acbfb0 | ingest.documents.raw_extraction |
| amount | 96000 |  |  | de074bf4-bb78-5fcb-833d-c200721b81a1 | ingest.documents.raw_extraction |
| date_2 | 2023-08-06 |  |  | f5a7455e-43c6-563e-bb94-da5639973546 | ingest.documents.raw_extraction |
| date_3 | 2023-08-11 |  |  | 0945dca5-8fe0-5f8b-bb0d-0c90cd159e29 | ingest.documents.raw_extraction |
| totals | {"cgst_rate": "9%", "igst_rate": null, "sgst_rate": "9%", "total_tax": 405.0, "cgst_amount": 202.5, "grand_total": 2655.0, "igst_amount": null, "sgst_amount": 202.5, "expenses_total": 750.0, "subtota… |  | {'cgst_rate': '9%', 'igst_rate': None, 'sgst_rate': '9%', 'total_tax': 405.0, 'cgst_amount': 202.5, 'grand_total': 2655.0, 'igst_amount': None, 'sgst_amount': 202.5, 'expenses_total': 750.0, 'subtota… | f9ba9850-3254-5409-8919-0fc8b1e6d627 | ingest.documents.raw_extraction |
| address | Surat |  |  | 49eedaf9-d77a-5f2f-a5d4-70674e36075f | ingest.documents.raw_extraction |
| gstin_2 | 24AABCB5730G1Z3 |  |  | 678d4869-29aa-52da-b276-9439a9ac5d6a | ingest.documents.raw_extraction |
| amount_2 | 1500.00 |  |  | e39c9348-b4aa-5267-844b-4807d1eb1705 | ingest.documents.raw_extraction |
| amount_3 | 750.00 |  |  | 406faafc-4b23-5f2e-aca6-66dd04a1ffd0 | ingest.documents.raw_extraction |
| amount_4 | 2250.00 |  |  | 99073406-2c63-5381-8963-c7e1b9a71d48 | ingest.documents.raw_extraction |
| amount_5 | 202.50 |  |  | 710e64e8-43e3-5933-85c9-7ef85176940f | ingest.documents.raw_extraction |
| amount_6 | 202.50 |  |  | 55762fd2-cb65-5db7-a889-1a99b5382989 | ingest.documents.raw_extraction |
| amount_7 | 405.00 |  |  | da9baa82-bab8-5630-af54-fc4f29f6474b | ingest.documents.raw_extraction |
| amount_8 | 2655.00 |  |  | 5474909b-3958-5c27-a55a-09ceac120b8a | ingest.documents.raw_extraction |
| address_2 | Vadodara |  |  | 704e3cc1-4ab9-5173-aa4b-79416b1cd2ce | ingest.documents.raw_extraction |
| pan_number | AJAPD3623K |  |  | 2370200f-39d0-5d7f-86ac-dc77bcebf2db | ingest.documents.raw_extraction |
| person_name | Vivekkumar M. Desai |  |  | 40ef1e72-2fb3-586b-8dfa-a2438abf8ad0 | ingest.documents.raw_extraction |
| claim_number | OC-24-2203-1801-00002600 |  |  | 25d236b9-bd17-5f7b-82af-1b5d293af92f | ingest.documents.raw_extraction |
| insured_name | Maheshkumar Vasava |  |  | 92eaf22c-2682-51d8-a9b6-bdf219e1cc6f | ingest.documents.raw_extraction |
| insurer_name | Bajaj Allianz General Insurance Co. Ltd. |  |  | 2f26a52e-f566-5bb1-b3bb-0bd9c636cc9d | ingest.documents.raw_extraction |
| policy_number | OG-24-2203-1801-06005412 |  |  | 156cf79d-43e2-5ba8-9dcd-f2a711c1731a | ingest.documents.raw_extraction |
| fees_breakdown | [{"rate": null, "amount": null, "description": "SPOT SURVEY", "serial_number": 1}, {"rate": null, "amount": 1500.0, "description": "FINAL SURVEY", "serial_number": 2}, {"rate": null, "amount": null, … |  | [{'rate': None, 'amount': None, 'description': 'SPOT SURVEY', 'serial_number': 1}, {'rate': None, 'amount': 1500.0, 'description': 'FINAL SURVEY', 'serial_number': 2}, {'rate': None, 'amount': None, … | 64588f90-6fcd-5cb7-9761-d53d5a260717 | ingest.documents.raw_extraction |
| survey_details | {"date_of_loss": "2023-08-06", "report_number": "VD/BAGIC/08/2023/6331", "date_of_survey": "2023-08-11", "place_of_supply": "GUJARAT", "state_of_supply": "GUJARAT"} |  | {'date_of_loss': '2023-08-06', 'report_number': 'VD/BAGIC/08/2023/6331', 'date_of_survey': '2023-08-11', 'place_of_supply': 'GUJARAT', 'state_of_supply': 'GUJARAT'} | 004def89-2c8d-5dfd-b915-4b793616a6d4 | ingest.documents.raw_extraction |
| vendor_details | {"vendor_pan": "AJAPD3623K", "vendor_name": "Vivekkumar M. Desai", "vendor_gstin": "24AJAPD2623K12N", "vendor_address": "29, Anand Nagar Society, Morabagad, Rander Road, Surat - 395005", "vendor_desi… |  | {'vendor_pan': 'AJAPD3623K', 'vendor_name': 'Vivekkumar M. Desai', 'vendor_gstin': '24AJAPD2623K12N', 'vendor_address': '29, Anand Nagar Society, Morabagad, Rander Road, Surat - 395005', 'vendor_desi… | f4ba3f8e-8404-5f75-82d1-cbab53cde06f | ingest.documents.raw_extraction |
| vehicle_details | {"make": "H Eon", "estimated_loss": "96000", "registration_number": "GJ27 AA 0736"} |  | {'make': 'H Eon', 'estimated_loss': '96000', 'registration_number': 'GJ27 AA 0736'} | 54f4f302-d337-5cad-a3db-0b80b1e8ade2 | ingest.documents.raw_extraction |
| customer_details | {"customer_name": "Bajaj Allianz General Insurance Co. Ltd. (Regional Office)", "customer_gstin": "24AABCB5730G1Z3", "customer_address": "4th Floor, Atlantis Heritage, Opp-Deepali Petrol Pump, Sarabh… |  | {'customer_name': 'Bajaj Allianz General Insurance Co. Ltd. (Regional Office)', 'customer_gstin': '24AABCB5730G1Z3', 'customer_address': '4th Floor, Atlantis Heritage, Opp-Deepali Petrol Pump, Sarabh… | 7a37eb29-a0ce-5300-9a03-4562449f4ac4 | ingest.documents.raw_extraction |
| insurance_linkage | {"claim_number": "OC-24-2203-1801-00002600", "insured_name": "MAHESHKUMAR VASAVA", "policy_number": "OG-24-2203-1801-06005412", "insurance_company": "Bajaj Allianz General Insurance Co. Ltd."} |  | {'claim_number': 'OC-24-2203-1801-00002600', 'insured_name': 'MAHESHKUMAR VASAVA', 'policy_number': 'OG-24-2203-1801-06005412', 'insurance_company': 'Bajaj Allianz General Insurance Co. Ltd.'} | b646fde7-665f-5b76-99d7-c2ec70be4183 | ingest.documents.raw_extraction |
| expenses_breakdown | [{"amount": null, "description": "PHOTOGRAPH", "serial_number": 1}, {"rate": 750.0, "amount": 750.0, "quantity": 1, "description": "CONVEYANCE CHARGES", "serial_number": 2}, {"amount": null, "descrip… |  | [{'amount': None, 'description': 'PHOTOGRAPH', 'serial_number': 1}, {'rate': 750.0, 'amount': 750.0, 'quantity': 1, 'description': 'CONVEYANCE CHARGES', 'serial_number': 2}, {'amount': None, 'descrip… | 77c1745f-1197-54d3-b5d7-c24cd214e78b | ingest.documents.raw_extraction |
| vehicle_registration | GJ27 AA 0736 |  |  | 8bad36a0-9cab-5905-a063-f67250b52498 | ingest.documents.raw_extraction |
| survey_fee_bill_number | 6331 |  |  | 9ea70aee-8444-5146-a443-1ce5465c2c64 | ingest.documents.raw_extraction |
| surveyor_license_number | S.I.A. 73760 |  |  | 5898742a-64a1-5165-9a80-6e96a2800ddd | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "Vendor header", "field_label": "Licence No.", "field_value": "S.I.A. 73760"}, {"section": "Vendor header", "field_label": "Valid upto", "field_value": "03rd Oct 2024"}, {"section": "Ven… |  | [{'section': 'Vendor header', 'field_label': 'Licence No.', 'field_value': 'S.I.A. 73760'}, {'section': 'Vendor header', 'field_label': 'Valid upto', 'field_value': '03rd Oct 2024'}, {'section': 'Ven… | 29dc3d15-5ba8-5260-b1f8-808645702e81 | ingest.documents.raw_extraction |
| reference_number_for_the_bill | 6331-28-2023-34 |  |  | 87863a07-7d79-584e-977c-374aa5c271f6 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `223233267_Signed_Licensed_Surveyor_Report` — `accident_report`  (row uuid `c41badf1-19c5-4485-97b2-f56624fa837f`)

**Fields (extracted_fields / raw_extraction JSONB):**

> _(no rows)_

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `223237590_Signed_Licensed_Surveyor_Report` — `accident_report`  (row uuid `77eb42f1-c639-40a6-a92c-42a2ac9ca221`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| date | 03-AUG-2023 |  |  | 17a93e4b-857c-5d00-afa1-9019522d3c40 | ingest.documents.raw_extraction |
| amount | 77942 |  |  | b5b0694a-fe11-5375-a7e3-9ea1c95c80f3 | ingest.documents.raw_extraction |
| date_2 | 08-AUG-2023 |  |  | 9127bdf1-9bf6-5593-95ef-b39d8bc439d8 | ingest.documents.raw_extraction |
| date_3 | 10-AUG-2023 |  |  | e3f43238-204a-5ab5-bb5e-a0e84bf065aa | ingest.documents.raw_extraction |
| date_4 | 12-AUG-2023 |  |  | e2a8df6a-fb79-5669-a802-ffb732357e30 | ingest.documents.raw_extraction |
| date_5 | 17-OCT-2013 |  |  | c02a37d8-80bc-59c7-8a0e-83468bdfcfb7 | ingest.documents.raw_extraction |
| address | NANA VARACHHA HOUSING SOCIETY, NANA VARACHHA DHAL, NANA VARACHHA, KAM-REJ ROAD, SURAT CITY, SURAT, GUJARAT 395006 |  |  | 0d70393e-c059-54b1-bcc8-9c10607e178a | ingest.documents.raw_extraction |
| amount_2 | 29369 |  |  | 5adc1af0-8659-5a24-9158-9eced5059d6d | ingest.documents.raw_extraction |
| amount_3 | 49573 |  |  | 1d747cbf-145a-582e-8a9b-fd24e3e37415 | ingest.documents.raw_extraction |
| amount_4 | 1000 |  |  | 30f2bf59-e26e-533c-91b6-24f476b6a4e0 | ingest.documents.raw_extraction |
| amount_5 | 21462 |  |  | acc916f4-6a09-5049-a8c6-91f00f016ca7 | ingest.documents.raw_extraction |
| location | SURAT |  |  | e4d4cd68-700a-51fa-a53a-798a0bf87c42 | ingest.documents.raw_extraction |
| dl_number | GUJ0510281370 |  |  | 94341b74-9c5d-5d98-b8b6-18a1ddcfcd89 | ingest.documents.raw_extraction |
| issue_date | 15-APR-2008 |  |  | 4e4cc9e0-a87a-5728-9602-ebb13dea86ae | ingest.documents.raw_extraction |
| driver_name | PRAKASHBHAI CHAUDARY |  |  | f398e4f6-30b5-5ee4-8fd2-1d2e93905d30 | ingest.documents.raw_extraction |
| expiry_date | 02-AUG-2024 |  |  | d9c30ebd-9db8-5960-8cdd-c7858b4077fe | ingest.documents.raw_extraction |
| person_name | U.M.Desai |  |  | cd318f6a-29bb-5f64-bd6b-ae41332ab0e5 | ingest.documents.raw_extraction |
| claim_number | OC-24-2203-1801-00002660 |  |  | bd1bb17d-05dd-5e5d-b7ee-66363a1dc6de | ingest.documents.raw_extraction |
| insured_name | MAHESHKUMAR VASAVA |  |  | 95f82381-f5b9-549e-b58f-29180d700f40 | ingest.documents.raw_extraction |
| parts_report | {"parts_categories": [{"items": [{"qty": 1, "net_tax": 0, "net_amount": 4939.3, "description": "GLASS-WINDSHIELD", "depreciation": 0, "retail_price": 4939.3, "total_amount": 4939.3, "assessed_amount"… |  | {'parts_categories': [{'items': [{'qty': 1, 'net_tax': 0, 'net_amount': 4939.3, 'description': 'GLASS-WINDSHIELD', 'depreciation': 0, 'retail_price': 4939.3, 'total_amount': 4939.3, 'assessed_amount'… | b9930612-ccdd-583e-822a-c709d19c9ce7 | ingest.documents.raw_extraction |
| phone_number | 9773228144 |  |  | def02f4a-eb5b-515c-8845-d2d5ae5cb17b | ingest.documents.raw_extraction |
| claim_details | {"claim_id": "31871257", "claim_number": "OC-24-2203-1801-00002660", "date_of_loss": "2023-08-08", "policy_number": "OC-24-2203-1801-0006512", "date_of_survey": "2023-08-12", "intimation_date": "[ill… |  | {'claim_id': '31871257', 'claim_number': 'OC-24-2203-1801-00002660', 'date_of_loss': '2023-08-08', 'policy_number': 'OC-24-2203-1801-0006512', 'date_of_survey': '2023-08-12', 'intimation_date': '[ill… | 8e00dc56-7a54-597b-a2d1-3c685b0418fb | ingest.documents.raw_extraction |
| engine_number | G3-1ADM199755 |  |  | 955daabe-5799-5646-9365-5d6af91640f6 | ingest.documents.raw_extraction |
| expiry_date_2 | 11-APR-2026 |  |  | ebd98e06-afc4-5c5b-aff9-7890234ce307 | ingest.documents.raw_extraction |
| policy_number | OC-24-2203-1801-0006512 |  |  | 9c07b425-0de6-5ca8-b3d5-5cc63bccb8aa | ingest.documents.raw_extraction |
| chassis_number | MALA351ALDM226944 |  |  | d61540b4-7a02-5a19-85f3-c3522e570010 | ingest.documents.raw_extraction |
| driver_details | {"driver_name": "PRAKASHBHAI CHAUDARY", "dl_endorsement": "LMVNT", "vehicle_parked": "No", "relation_with_phi": "Friend", "driving_license_type": "Permanent", "mdl_issuing_authority": "SURAT", "drivi… |  | {'driver_name': 'PRAKASHBHAI CHAUDARY', 'dl_endorsement': 'LMVNT', 'vehicle_parked': 'No', 'relation_with_phi': 'Friend', 'driving_license_type': 'Permanent', 'mdl_issuing_authority': 'SURAT', 'drivi… | 9edf3536-1633-5cc1-88b2-7cc328b01bee | ingest.documents.raw_extraction |
| vehicle_details | {"make": "HYUNDAI", "color": "Metallic", "model": "EON", "engine_number": "G3-1ADM199755", "hypothecation": "[not specified]", "chassis_number": "MALA351ALDM226944", "cubic_capacity": "[not specified… |  | {'make': 'HYUNDAI', 'color': 'Metallic', 'model': 'EON', 'engine_number': 'G3-1ADM199755', 'hypothecation': '[not specified]', 'chassis_number': 'MALA351ALDM226944', 'cubic_capacity': '[not specified… | 1fb89263-3581-5618-b532-a54f9847e76d | ingest.documents.raw_extraction |
| customer_details | {"customer_name": "MAHESHKUMAR VASAVA", "mobile_number": "9773228144", "customer_address": "NANA VARACHHA HOUSING SOCIETY, NANA VARACHHA DHAL, NANA VARACHHA, KAM-REJ ROAD, SURAT CITY, SURAT, GUJARAT … |  | {'customer_name': 'MAHESHKUMAR VASAVA', 'mobile_number': '9773228144', 'customer_address': 'NANA VARACHHA HOUSING SOCIETY, NANA VARACHHA DHAL, NANA VARACHHA, KAM-REJ ROAD, SURAT CITY, SURAT, GUJARAT … | 2c7687e0-fd5d-5b57-991a-ef60d15f3d3b | ingest.documents.raw_extraction |
| loss_description | As per claim form insured states that while IV was proceeding on its way at that time in process to save TP motor cyclist IV dashed with divider from front side thereby IV sustain damages |  |  | 14033659-c0a7-557b-aaaf-e195d427175a | ingest.documents.raw_extraction |
| repairer_details | {"repairer_name": "NAVJIVAN MOTORS PVT LTD."} |  | {'repairer_name': 'NAVJIVAN MOTORS PVT LTD.'} | 77ace883-2580-59b8-96a4-9fa8a4772739 | ingest.documents.raw_extraction |
| organization_name | NAVJIVAN MOTORS PVT LTD. |  |  | fbf8b652-91f5-5e43-8e37-560d0439a2e7 | ingest.documents.raw_extraction |
| surveyor_comments | Survey conducted physically Odometer is not working due to accident hence photo not available RC VIN and VIN number verified Close proxy case insurer are advice to check the actual driver and Date of… |  |  | ea9f785f-6bec-518b-b79d-52461b131d34 | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AA0736 |  |  | 59ff3ac1-d8ff-5194-a3ef-c7c78fef9a07 | ingest.documents.raw_extraction |
| claim_id_for_parts_report | 31871257 |  |  | e3d55aeb-f74b-57e4-af4c-5b37dc4e8b98 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `223404609_Follow-up_Letters` — `correspondence`  (row uuid `d840dc4f-a181-4f72-b0ce-f255a9bdc49f`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| date | 2023-08-18 |  |  | 7e279ee9-ec1a-5988-a3b9-feec8a4e9834 | ingest.documents.raw_extraction |
| location | Vadodara |  |  | dcf67340-9f34-5219-bd2d-c12a7573d3ad | ingest.documents.raw_extraction |
| claim_number | OC-24-2218-1801-005412 |  |  | 3ac8420d-a7b6-5b2e-a983-73ddc795edd7 | ingest.documents.raw_extraction |
| insurer_name | Bajaj Allianz General Insurance Co. Ltd. |  |  | 26fb9644-4a9d-5c9d-9790-b8fa39e9d66e | ingest.documents.raw_extraction |
| claimant_name | Mr. Maheshwaram Indrasingh Vasava |  |  | c3929361-947c-5cfb-925b-52c6ecdcdc84 | ingest.documents.raw_extraction |
| policy_number | OC-2L-3207-1801-2660 |  |  | 8ed26826-f591-5c2b-9991-502a43e8ad4e | ingest.documents.raw_extraction |
| letter_content | {"key_points": ["Claim has been reported with documents submitted", "RDA approval has been obtained", "Vehicle was not thrown at time of accident", "Clarification requested within seven days", "All p… |  | {'key_points': ['Claim has been reported with documents submitted', 'RDA approval has been obtained', 'Vehicle was not thrown at time of accident', 'Clarification requested within seven days', 'All p… | 1393821b-a910-5a73-b5c8-971af0c88964 | ingest.documents.raw_extraction |
| claim_reference | {"claim_number": "OC-24-2218-1801-005412", "policy_reference": "OC-2L-3207-1801-2660", "claim_number_original_script": "OC-24-2218-1801-005412", "policy_reference_original_script": "OC-2L-3207-1801-2… |  | {'claim_number': 'OC-24-2218-1801-005412', 'policy_reference': 'OC-2L-3207-1801-2660', 'claim_number_original_script': 'OC-24-2218-1801-005412', 'policy_reference_original_script': 'OC-2L-3207-1801-2… | 69467a96-1bb1-5ad7-a93e-0ae522c64988 | ingest.documents.raw_extraction |
| insured_details | {"insured_name": "Mr. Maheshwaram Indrasingh Vasava", "insured_name_original_script": "Mr. Maheshwaram Indrasingh Vasava"} |  | {'insured_name': 'Mr. Maheshwaram Indrasingh Vasava', 'insured_name_original_script': 'Mr. Maheshwaram Indrasingh Vasava'} | 47cb604a-1c29-50b7-a520-c35e00da6ab1 | ingest.documents.raw_extraction |
| contact_information | {"email": "bagshelp@bajajallianz.co.in", "phone": null, "website": "www.bajajallianz.com", "office_address": "4th Floor, Atlantis Heritage, B/H Atlantis Heights, Opp. Swagat Petrol Pump, Sarabhai Mai… |  | {'email': 'bagshelp@bajajallianz.co.in', 'phone': None, 'website': 'www.bajajallianz.com', 'office_address': '4th Floor, Atlantis Heritage, B/H Atlantis Heights, Opp. Swagat Petrol Pump, Sarabhai Mai… | 1c61ffa3-79b0-5ef9-b972-0335533888a4 | ingest.documents.raw_extraction |
| correspondence_details | {"letter_type": "Claim Clarification Request", "date_of_letter": "2023-08-18", "issuing_address": "4th Floor, Atlantis Heritage, B/H Atlantis Heights, Opp. Swagat Petrol Pump, Sarabhai Main Road, Vad… |  | {'letter_type': 'Claim Clarification Request', 'date_of_letter': '2023-08-18', 'issuing_address': '4th Floor, Atlantis Heritage, B/H Atlantis Heights, Opp. Swagat Petrol Pump, Sarabhai Main Road, Vad… | eb026812-1eec-54ca-b0b4-72b0f3ba41ba | ingest.documents.raw_extraction |
| barcode_number_on_document | RG289062596IN |  |  | 9716903f-e9a8-5ddd-b1ad-0965d04ae9bd | ingest.documents.raw_extraction |
| additional_extracted_fields | [{"section": "Header", "field_label": "Company Registration", "field_value": "A Company incorporated under the Companies Act, 1956"}, {"section": "Header", "field_label": "Registered Office", "field_… |  | [{'section': 'Header', 'field_label': 'Company Registration', 'field_value': 'A Company incorporated under the Companies Act, 1956'}, {'section': 'Header', 'field_label': 'Registered Office', 'field_… | ee17390e-7f87-5851-8a41-70f50b02111a | ingest.documents.raw_extraction |
| corporate_identification_number_of_bajaj | U66010PN2000PLC015329 |  |  | 3ac7b9f2-31d4-5fd8-8514-0c5943d046a5 | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

### Doc `223721550_Follow-up_Letters` — `correspondence`  (row uuid `175c77eb-c1b3-4e13-bb88-0c420c2abee3`)

**Fields (extracted_fields / raw_extraction JSONB):**

| canonical_key | value | confidence | raw_value | source_field_id | storage |
| --- | --- | --- | --- | --- | --- |
| address | Surat City, Surat, Gujarat |  |  | 3629fc10-2c04-5e9f-87b9-b96bae2e1d21 | ingest.documents.raw_extraction |
| location | Vadodara, Gujarat |  |  | 4d13cbab-4b27-5ce7-abe5-7690a79d4ac9 | ingest.documents.raw_extraction |
| location_2 | Pune |  |  | ef85323f-97be-5066-8121-d8865bbb3d64 | ingest.documents.raw_extraction |
| person_name | Bipin Shiroya |  |  | f993cf8f-5397-50d9-93e9-20778721f077 | ingest.documents.raw_extraction |
| claim_number | OC-24-2203-1801-00002660 |  |  | ec3ac075-75fa-5830-a8aa-eb5b9597204a | ingest.documents.raw_extraction |
| insurer_name | Bajaj Allianz General Insurance Company Limited |  |  | 63d96f49-18b8-5f29-afa1-3f35f88754a9 | ingest.documents.raw_extraction |
| phone_number | 9537436355 |  |  | 436f15e1-88eb-59a3-9fa9-5decda2fa709 | ingest.documents.raw_extraction |
| claimant_name | Mr. Maheshkumar Indrasing Vasava |  |  | bf893b83-6997-5c22-9df6-0e93ba387ba6 | ingest.documents.raw_extraction |
| policy_number | OG-24-2203-1801-00005412 |  |  | 3dbe1b3e-8c87-53f0-88a3-1e0152f2c279 | ingest.documents.raw_extraction |
| phone_number_2 | 0265-3960861 |  |  | 10c5d622-adbc-5001-9ebd-fc2645434e62 | ingest.documents.raw_extraction |
| phone_number_3 | +91-9898994381 |  |  | 9a1e46ca-ff38-56b7-b09c-ebf9f2652a79 | ingest.documents.raw_extraction |
| phone_number_4 | 7507245858 |  |  | e3c56b84-1c19-5347-b584-c03300c68ed1 | ingest.documents.raw_extraction |
| phone_number_5 | 8308943060 |  |  | bcb1c49e-d3ad-52e6-b3b9-d5b8c7b0ac2a | ingest.documents.raw_extraction |
| phone_number_6 | 1800-209-5858 |  |  | 18c8d7dc-a3cb-5861-908a-1df1bd2a2983 | ingest.documents.raw_extraction |
| claim_reference | {"loss_date": "2023-08-08", "claim_number": "OC-24-2203-1801-00002660", "insured_name": "Mr. Maheshkumar Indrasing Vasava", "policy_number": "OG-24-2203-1801-00005412", "vehicle_number": "GJ27AA0736"… |  | {'loss_date': '2023-08-08', 'claim_number': 'OC-24-2203-1801-00002660', 'insured_name': 'Mr. Maheshkumar Indrasing Vasava', 'policy_number': 'OG-24-2203-1801-00005412', 'vehicle_number': 'GJ27AA0736'… | 1a814bd7-078f-5de2-b9a8-5e0138682e14 | ingest.documents.raw_extraction |
| insured_details | {"name": "Mr. Maheshkumar Indrasing Vasava", "phone": "9537436355", "address": "6 Nana Varachha Housing Society, Nana Varachha Dhal., Kamrej Road, Surat City, Surat, Gujarat-395006", "original_script… |  | {'name': 'Mr. Maheshkumar Indrasing Vasava', 'phone': '9537436355', 'address': '6 Nana Varachha Housing Society, Nana Varachha Dhal., Kamrej Road, Surat City, Surat, Gujarat-395006', 'original_script… | fc52f242-75a1-5046-b841-9079385e023b | ingest.documents.raw_extraction |
| issuing_authority | {"company_name": "Bajaj Allianz General Insurance Company Limited", "office_address": "Bajaj Allianz General Insurance Company Ltd., 4th Floor, Atlantis Heritage, Behind Atlantis Heights, Opp Swagat … |  | {'company_name': 'Bajaj Allianz General Insurance Company Limited', 'office_address': 'Bajaj Allianz General Insurance Company Ltd., 4th Floor, Atlantis Heritage, Behind Atlantis Heights, Opp Swagat … | dfddab32-b8e4-5e51-b4fa-a248fbf0824e | ingest.documents.raw_extraction |
| contact_information | {"email": "bagchelp@bajajallianz.co.in", "mobile": "+91-9898994381", "website": "www.bajajallianz.com", "landline": "0265-3960861", "sms_code": "QUERY to 575758", "whatsapp": "7507245858", "toll_free… |  | {'email': 'bagchelp@bajajallianz.co.in', 'mobile': '+91-9898994381', 'website': 'www.bajajallianz.com', 'landline': '0265-3960861', 'sms_code': 'QUERY to 575758', 'whatsapp': '7507245858', 'toll_free… | cd0e0146-96e6-5a7b-99e8-ec339d18a82b | ingest.documents.raw_extraction |
| grievance_redressal | {"procedure_url": "https://www.bajajallianz.com/about-us/customer-service.html"} |  | {'procedure_url': 'https://www.bajajallianz.com/about-us/customer-service.html'} | d3577e36-def1-524a-adb4-a092b62fab5b | ingest.documents.raw_extraction |
| repudiation_details | {"letter_date": "2023-09-21", "repudiation_reason": "Insured failed to respond with clarification submission and proper documentary evidences till date as per requirement for further review of claim"… |  | {'letter_date': '2023-09-21', 'repudiation_reason': 'Insured failed to respond with clarification submission and proper documentary evidences till date as per requirement for further review of claim'… | fae5ecf5-379b-56b1-931f-5402dfb28ba6 | ingest.documents.raw_extraction |
| vehicle_registration | GJ27AA0736 |  |  | d7182016-69d5-52a4-8760-0fb50a60a5fc | ingest.documents.raw_extraction |
| irdai_registration_number | 113 |  |  | 7f71b964-2429-51ec-b964-bdad4803384d | ingest.documents.raw_extraction |
| corporate_identification_number_(cin) | U66010PN2000PLC015329 |  |  | 0ddaf7f5-f141-56c4-aeef-4a877e1f04bc | ingest.documents.raw_extraction |

**Critical identifiers (`ingest.critical_identifiers`):**

> _(no rows)_

**Semantic extraction (clean shape):**

```json

```

## D — Facts

Total facts: **546**

| fact_id | fact_type | fact_text | confidence | doc (filename / ext_id / type) | source_field_ids | page | entities_count |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2acd65f9-f61c-45d1-a7b9-0ece42a9919c | PERSONAL_INFO | The contact mobile number is +919727635960. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | edbd38b3-a35c-5aee-b87e-773de51ca6e3, 6bf55dc5-3ae4-5d44-80e2-7d1a4b1c40c6 |  | 1 |
| c017cd96-ab70-40f4-8ff6-9394199ba1a0 | DATE_TIME | The cash receipt date is 2023-08-08. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 4aabf8b7-ab11-5c0d-a2d4-881b6bde9e17 |  | 1 |
| 2ff81d24-caa3-4aa8-8f09-6843afa14c0c | FINANCIAL | The cash receipt number is GJ230808C9783109. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 20d50f0d-6952-54ee-af07-8278a0bd8db7, 4aabf8b7-ab11-5c0d-a2d4-881b6bde9e17 |  | 1 |
| c064a021-868e-4af8-a57e-97ac0a61f4cc | FINANCIAL | The particular fee amount is INR 200. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 551c2d54-525a-5fa4-8487-3714ade8492a |  | 1 |
| 61792c7c-f500-4935-b440-ad890f040f23 | DATE_TIME | The finance is valid until 2028-10-18. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 9b476a8d-8ca9-5d78-bb14-740bb29d9bd1 |  | 1 |
| 82871375-9d0a-4e37-9250-a147bb5d12e2 | FINANCIAL | The financer is BAJAJ FINANCE LIMITED. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | cdbed2f8-efde-549e-b0e7-c19b51cabbf0, 9b476a8d-8ca9-5d78-bb14-740bb29d9bd1 |  | 1 |
| 1915fb53-8702-448b-ab41-771232ae85c5 | LOCATION | The financer address is OFFICE 301 TO 311 3RD FL, UNIVERSALBUSINESS CENTER L.P.SAVANI ROADNEAR MADHURAM CIRCLE ADAJAN, Surat-395009. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | cdbed2f8-efde-549e-b0e7-c19b51cabbf0, 54956e21-3263-5770-ad62-025471d179a0, 9b476a8d-8ca9-5d78-bb14-740bb29d9bd1 |  | 1 |
| 6dd84fde-f8da-4bba-9641-5796cb511975 | DATE_TIME | The vehicle was registered on 2013-10-17. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| 5aef3a07-be34-4cb5-8fd0-bf4320d6bb1f | VEHICLE_INFO | The vehicle registration number is GJ27AK0736. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45, cb053bad-36eb-5b9e-a1ca-cea5d70d2c8d |  | 1 |
| 8a23967d-87d2-46fa-ae22-e1575a4d3499 | VEHICLE_INFO | The vehicle fuel type is PETROL. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| 19ee9e0b-0c7a-4a84-80e6-5b29d53b4ff6 | DATE_TIME | The vehicle manufacturing month and year is 08/2013. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| 13c4d372-a5a9-4923-bc59-d76f7c323f1b | VEHICLE_INFO | The vehicle motor use code is 3. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document |  |  | 1 |
| 4f9b50a6-65e5-483e-82bc-6ff710c758fa | VEHICLE_INFO | The vehicle status is Active. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 1266d20b-da28-57d1-80be-08689d82edd8 |  | 1 |
| 9d4fa10e-fd24-4801-90d7-ce360dd61d96 | VEHICLE_INFO | The application number for registration is GJ230808V2160368. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 526778ec-b1fd-54bc-838d-aef5144ac7fe, 189290e2-bf97-5918-a399-2d60b5116213 |  | 1 |
| abe0f5e0-07b5-46a5-a61a-da61ed015efe | FINANCIAL | The tax amount is INR 20634. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 769f23ec-9df5-56ba-a28c-7c5c7fd925ac, 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| 73c9d2d8-0c39-47ea-b008-92d59674a65c | CLAIM_DETAIL | The insurer is Bajaj Allianz General Insurance Co. Ltd. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | e79bd31f-68e8-5ab7-bcd4-10ba696a9848, d3ce9a87-d817-52e0-ad05-e0e3f85353e9 |  | 1 |
| dcd95dfe-5d04-4c73-855f-1fb6eb44e211 | DATE_TIME | The insurance policy is valid from 2023-08-03 to 2024-08-02. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | d3ce9a87-d817-52e0-ad05-e0e3f85353e9 |  | 2 |
| fc9238c7-e34b-4fe1-800f-2429722c6dae | CLAIM_DETAIL | The insurance policy number is OG-24-2203-1801-0005412. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | c8945762-dbd1-5c59-b17c-87ec552485c9, d3ce9a87-d817-52e0-ad05-e0e3f85353e9 |  | 1 |
| a06c4254-c77d-4598-8f2f-21f65dd81a4a | LOCATION | The vehicle owner address is C/O NEW VARGHIA HOUSING SOCIETY(KAMREJ) ROAD DHAL, Surat Gujarat-395006. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 09a1af78-134a-55c3-86bd-94a0c5c8f9af, 54956e21-3263-5770-ad62-025471d179a0, 9fcf74bb-a76b-5b27-b049-c0583008e1d3 |  | 1 |
| 6dbd321c-f61a-4626-83b5-e386fac2e466 | PERSONAL_INFO | The vehicle owner is MAHESH KUMAR. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 09a1af78-134a-55c3-86bd-94a0c5c8f9af, f031d491-8be2-5218-a9d7-fcaeefab8dc3 |  | 1 |
| fef58a8f-574f-4f92-8712-d25a91c0e427 | VEHICLE_INFO | The vehicle emission standard is EURO 4. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| a7d0fc69-1c02-41e0-9a99-970476d47b5f | VEHICLE_INFO | The vehicle wheel base is 2380 mm. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| d24c6e90-ab6f-489b-b935-4711b1ac32e5 | VEHICLE_INFO | The vehicle laden weight is 1210 kg. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| 7125e88f-8d24-4af7-9ae9-ca1f08754f37 | VEHICLE_INFO | The vehicle seating capacity including driver is 5. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document |  |  | 1 |
| b00d8feb-a758-43f4-a717-81451cacefbf | VEHICLE_INFO | The vehicle has 3 cylinders. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document |  |  | 1 |
| 895cd2cd-ad95-4e48-a86e-87356549bf1d | VEHICLE_INFO | The vehicle cubic capacity is 814.00 cc. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | e6a0f5b2-3f31-5633-8be0-49dfaed6d094 |  | 1 |
| d658fcbc-2dd0-4827-bfa7-875a69936b92 | VEHICLE_INFO | The vehicle model is EGH SPORTZ 0.8IN. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| 8f739a0a-153a-469f-866a-352df8256e66 | VEHICLE_INFO | The vehicle make is HYUNDAI MOTOR INDIA LTD. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45, c5e5ee24-ebd6-5d5a-bbb6-f8b01cb36237 |  | 1 |
| a8aa2997-76e2-491a-a675-5057111e4d43 | VEHICLE_INFO | The vehicle engine number is G3H4DM199755. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45, 20afd3d5-f5a7-53ff-a1fb-b0bd921822e6 |  | 1 |
| 3a434b7c-3eaf-4d24-9a60-5e6ff73199ea | VEHICLE_INFO | The vehicle chassis number is MALASIYALDA226944. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45, ab838704-e5e4-533b-a08e-d726f180481a |  | 1 |
| d6130286-b5a9-4465-94d0-c1fc7bb76710 | DATE_TIME | The vehicle registration is valid until 2028-10-16. | 0.95 | 218890832_Registration_Certificate.jpg / 218890832_Registration_Certificate / vehicle_document | 30ca7b37-f422-5c0a-a7d2-1daca633fc45 |  | 1 |
| 693eec52-e0f0-42f8-a101-872330315482 | CLAIM_DETAIL | The driving license number is GJ05/028137/06. | 0.98 | 218890867_Motor_Driving_License_(MDL).jpg / 218890867_Motor_Driving_License_(MDL) / driving_license |  |  | 1 |
| 9485343d-fedc-47b8-928f-644b9e507369 | DATE_TIME | The license was issued on 2006-04-15. | 0.98 | 218890867_Motor_Driving_License_(MDL).jpg / 218890867_Motor_Driving_License_(MDL) / driving_license |  |  | 1 |
| 9e3971b3-43d3-4666-860b-470c69b8ef1e | PERSONAL_INFO | The license holder name is Chaudhari Prakashbhai Manjibhai. | 0.98 | 218890867_Motor_Driving_License_(MDL).jpg / 218890867_Motor_Driving_License_(MDL) / driving_license |  |  | 1 |
| 8c457bc6-0aea-4708-81d8-d81522b7909b | LOCATION | The license holder's address is A/P-Balaibuva, Tal-Umarpada, Surat 394540. | 0.98 | 218890867_Motor_Driving_License_(MDL).jpg / 218890867_Motor_Driving_License_(MDL) / driving_license |  |  | 1 |
| 25de760f-2fd3-4ab5-90d4-47c5845863e1 | PERSONAL_INFO | The license holder's date of birth is 1987-09-07. | 0.98 | 218890867_Motor_Driving_License_(MDL).jpg / 218890867_Motor_Driving_License_(MDL) / driving_license |  |  | 1 |
| e414e212-12e9-4b5d-91c7-aeb3371ee6cd | VEHICLE_INFO | The license holder is authorized to drive Light Motor Vehicles (LMV) from 2006-04-12. | 0.70 | 218890867_Motor_Driving_License_(MDL).jpg / 218890867_Motor_Driving_License_(MDL) / driving_license |  |  | 2 |
| 698de4b4-a254-476f-8f3d-998c56037611 | DATE_TIME | The license validity for transport vehicles is from 2006-04-12 to 2026-04-11. | 0.90 | 218890867_Motor_Driving_License_(MDL).jpg / 218890867_Motor_Driving_License_(MDL) / driving_license |  |  | 2 |
| f075e53a-54ba-4ef9-b02c-239dc126fb9b | VEHICLE_INFO | The license is valid for motorcycles up to 50cc and other specified vehicle classes. | 0.85 | 218890867_Motor_Driving_License_(MDL).jpg / 218890867_Motor_Driving_License_(MDL) / driving_license |  |  | 1 |
| 59700fed-ee27-4d7d-83c7-918255bae082 | PERSONAL_INFO | The issuing RTO for the driving license is UJSLO7. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 283f6cfc-c1f3-51d9-90aa-1e7ecc8e04ff |  | 0 |
| f2a755e3-6391-4763-a343-32e1531e3c9f | PERSONAL_INFO | The driver name is FIR HADI H HDYAR ISHAHDI. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 41b2536e-723c-5262-aa53-9b1967335651, 283f6cfc-c1f3-51d9-90aa-1e7ecc8e04ff |  | 1 |
| 5c8d6f0f-7126-436a-b519-8304f56a13b3 | LOCATION | The place of accident is Nema Vasselley city. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 6a0d3ddc-3b6f-59b3-a578-248116d49115, ad47b3e7-bb65-5557-9846-d478bc6a2c74, 29d0dab6-e02b-530e-b28c-0dd2b59fd45c |  | 1 |
| a5c5907e-e91c-4147-89b5-4d7e08f7e26a | INCIDENT | The number of occupants in the vehicle at the time of accident was 02. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | aa83e587-764c-5dd1-8335-463a5e6b88b4 |  | 0 |
| 3ab40841-46dc-480b-b540-648e302f2775 | VEHICLE_INFO | The vehicle registration number is CA 2 #AA 0#36. | 0.40 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 4469a6d2-9c66-53da-a5ff-105956a12619, ad47b3e7-bb65-5557-9846-d478bc6a2c74, 03080231-7995-5412-8f93-1b0aef1c6706 |  | 1 |
| f7dfd825-e084-48bf-a943-f731bdefe3bc | PERSONAL_INFO | The insured state is BIHAR. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 44c22391-dbd2-564c-bb8e-683a2eafdd79, 6d827c66-88ee-5564-a2a6-c72d4232a47d, 03080231-7995-5412-8f93-1b0aef1c6706 |  | 1 |
| 053513d0-650d-4dcf-a645-447ef83eb5b3 | PERSONAL_INFO | The insured pin code is 841601. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 428738d7-5801-5617-b66a-89035e188d9d, 44c22391-dbd2-564c-bb8e-683a2eafdd79 |  | 1 |
| 795a22de-e1e7-44b3-8186-2f1d2590fa8c | PERSONAL_INFO | The insured city is GUNAMI. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 44c22391-dbd2-564c-bb8e-683a2eafdd79 |  | 1 |
| 15a18643-76c4-4b02-b013-52a4680c43dc | CLAIM_DETAIL | The policy number is OC-24-9003-1801-0000 2660. | 0.95 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | ed6f71e3-59b5-5452-b8e1-3e1b5c775bb9, 44c22391-dbd2-564c-bb8e-683a2eafdd79 |  | 1 |
| 3c344931-1c1c-447b-b03c-f8e7dda52359 | PERSONAL_INFO | The insured name is DRAM E3 H HDYAR. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | be7dbba9-b9da-5f65-b521-63dc7dca1bdd, 44c22391-dbd2-564c-bb8e-683a2eafdd79, 03080231-7995-5412-8f93-1b0aef1c6706 |  | 1 |
| 05aa5e1b-6bff-425b-88e6-7f0f924ca948 | PERSONAL_INFO | The insured address is GUNAMI VORBAD 4. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 44c22391-dbd2-564c-bb8e-683a2eafdd79 |  | 1 |
| a5476ca6-b520-4147-a9dc-f26dfa8f58d0 | PERSONAL_INFO | The signatory name is MAHA 3 HDYAR. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 425914a8-7792-5126-a99d-ec03bf364f94, 03080231-7995-5412-8f93-1b0aef1c6706, 7507bea6-3ec6-5ac3-a00a-a43811a71348 |  | 1 |
| 49448605-681f-4396-807a-278e2ddfa56d | CLAIM_DETAIL | The claim is for own damage. | 0.95 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | fe36999f-8161-53e8-bd21-f50093b00c42 |  | 0 |
| c8a6bfda-3180-4b28-b49b-2e5f9241efd6 | CLAIM_DETAIL | The document is a motor insurance claim form. | 0.95 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | 926ea072-0148-514e-8bc9-e887bc4545ad |  | 0 |
| 52223c3e-6fa7-4dc2-b9fb-3136b8fe9ad2 | CLAIM_DETAIL | The insurer is Bajaj Allianz General Insurance Company Limited. | 0.95 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | a21d933b-61fe-5530-b656-27dedbc1acc4 |  | 1 |
| 72d53dbb-0f84-4347-8f06-989b343ed57d | DATE_TIME | The claim form was signed on 2025-04-10. | 0.80 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | c8bd3410-27c4-5697-ab31-930e56095b9c, 03080231-7995-5412-8f93-1b0aef1c6706, 7507bea6-3ec6-5ac3-a00a-a43811a71348 |  | 1 |
| 76995883-fa5b-4bb4-8a57-b367b6d75cc1 | PERSONAL_INFO | The driving license number is UJOSIO0 2HADI061. | 0.50 | 218890910_Claim_Form.jpg / 218890910_Claim_Form / claim_form | c19564fc-51aa-563b-9525-5b838a24f812, 283f6cfc-c1f3-51d9-90aa-1e7ecc8e04ff |  | 1 |
| 203549fe-66bd-4e02-9396-ac3b25cb51d9 | CLAIM_DETAIL | An estimate for repairs from the repairer where the vehicle is to be repaired is required for accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| 556b7512-285d-4d1e-8e50-875f4e79f419 | CLAIM_DETAIL | A copy of the Motor Driving Licence of the person driving the vehicle at the material time is required for accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| 195bec79-fb67-4ac4-9a8c-14a04952c041 | CLAIM_DETAIL | A copy of the Registration Book and Tax Receipt is required for accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| b0248ef1-6f64-4848-9e90-aab92320538c | CLAIM_DETAIL | Proof of insurance policy or covermote copy is required for accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| fdf273b9-006d-42d0-91e0-6bac858c7339 | CLAIM_DETAIL | A duly filled and signed claim form is required for accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| f135206b-376c-4dee-a104-594fa1f98cee | CLAIM_DETAIL | Documents must be submitted to the nearby Bajaj Allianz Office for claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 1 |
| 4dcc6957-18a4-4570-af2a-d587c77330ff | CLAIM_DETAIL | AML and KYC documents as per guidelines are required for accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| 7b99a7dc-af95-4d18-8bb0-1bd93736350c | CLAIM_DETAIL | A Claims Discharge Cum Satisfaction Voucher signed across a Revenue Stamp is required for accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| 95dfca9b-865b-4961-af83-cd5e73146ff0 | CLAIM_DETAIL | Additional documents are required for commercial vehicle accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| 6a23e523-7701-4a71-91ab-ca85d32efcf3 | CLAIM_DETAIL | Permit, Fitness and Load Challan are required for commercial vehicle accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| 224a3236-ac01-4cfd-addb-d945a720eb6c | CLAIM_DETAIL | Repair bills and payment receipts after job completion are required for accident claim settlement. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| b80dfeb4-4b7b-4378-875d-6af9a3b02d4f | CLAIM_DETAIL | Police Panchanama or FIR is required for accident claim settlement in case of Third Party property damage, Death, or Body Injury. | 0.95 | 218890942_Claim_Form.jpg / 218890942_Claim_Form / correspondence |  |  | 0 |
| 72e22403-9e09-4c9c-83b7-4b4ac44fe8b0 | LOCATION | The workshop primary address is Near SMC Udhna South Zone Office, Devchand Nagar, Udhna, Surat. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | c65231ed-aca0-5f43-8a7d-a6f09b72cc2e |  | 1 |
| 898c1348-f554-4e39-ae9e-9b0de53055d8 | PERSONAL_INFO | The workshop branch office phone is (0261) 2855 777 or (0261) 2858 777. | 0.90 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | c65231ed-aca0-5f43-8a7d-a6f09b72cc2e |  | 1 |
| ec04abd0-f0f4-4358-b4f2-9c845e7968dd | INCIDENT | Front bumper replacement is approved. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | ca0ce261-f6c5-5bbe-928b-5fbf49d2e55c, b6e61f8e-9ac2-5af2-a39d-078771fcf49d, 1bf8e66c-3d52-54f9-8e12-0bf3c5255826 |  | 1 |
| 2035e227-ce7e-416d-ad26-300ff02acbaf | INCIDENT | Rear bumper replacement is approved. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | ca0ce261-f6c5-5bbe-928b-5fbf49d2e55c, b6e61f8e-9ac2-5af2-a39d-078771fcf49d, 1bf8e66c-3d52-54f9-8e12-0bf3c5255826 |  | 1 |
| 0fdeda31-d95f-4db0-ac85-ec028ff0976f | INCIDENT | Lower grille replacement is approved. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | ca0ce261-f6c5-5bbe-928b-5fbf49d2e55c, b6e61f8e-9ac2-5af2-a39d-078771fcf49d, 1bf8e66c-3d52-54f9-8e12-0bf3c5255826 |  | 1 |
| b9dad985-8526-4618-8a92-fe193c085fb8 | INCIDENT | Right-hand fender replacement is approved. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | ca0ce261-f6c5-5bbe-928b-5fbf49d2e55c, b6e61f8e-9ac2-5af2-a39d-078771fcf49d, 1bf8e66c-3d52-54f9-8e12-0bf3c5255826 |  | 1 |
| 0709eac0-de14-45af-8da6-4bc301fb06b9 | INCIDENT | Left-hand fender replacement is approved. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | ca0ce261-f6c5-5bbe-928b-5fbf49d2e55c, b6e61f8e-9ac2-5af2-a39d-078771fcf49d, 1bf8e66c-3d52-54f9-8e12-0bf3c5255826 |  | 1 |
| 8ab83020-728e-411a-b2cb-46af74408cc6 | INCIDENT | Headlighter replacement is approved. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | ca0ce261-f6c5-5bbe-928b-5fbf49d2e55c, b6e61f8e-9ac2-5af2-a39d-078771fcf49d, 1bf8e66c-3d52-54f9-8e12-0bf3c5255826 |  | 1 |
| 01ab2aac-ad9e-49db-88f9-1daca197d806 | INCIDENT | Condensor replacement is approved. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | ca0ce261-f6c5-5bbe-928b-5fbf49d2e55c, b6e61f8e-9ac2-5af2-a39d-078771fcf49d, 1bf8e66c-3d52-54f9-8e12-0bf3c5255826 |  | 1 |
| a1abc1f2-f883-43ae-abca-c21551c8ec51 | FINANCIAL | Touching/painting labor charge is INR 8,000. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | b6e61f8e-9ac2-5af2-a39d-078771fcf49d, 3ee7778a-0e21-5d33-8a61-a9de553f8303 |  | 1 |
| 35207936-fcd8-4046-b5b2-0e2c1a0d29be | FINANCIAL | An insurance excess of INR 1,000 is noted on the repair estimate. | 0.50 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | acf08aaf-0207-5a6d-b0ab-1d01f5477f4b |  | 1 |
| 78fe66e4-8c97-4d0c-bbd8-5db197efd6dd | LOCATION | The workshop branch office is located at Tulsi Krupa Arcade, Bis. Dr. House, Parvat Patiya, Puna Kumbhariya Road, Surat. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | c65231ed-aca0-5f43-8a7d-a6f09b72cc2e |  | 1 |
| 22d4a098-169e-4650-982c-a785f80ed38b | PERSONAL_INFO | The workshop email is bodyshop@navjivanhydundai.com. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | c65231ed-aca0-5f43-8a7d-a6f09b72cc2e |  | 1 |
| 8fe90c82-1d3a-4f89-9dc9-0c26e5a81833 | PERSONAL_INFO | The workshop primary contact phone is +91-261-3206002 or +91-261-3206003. | 0.90 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | c65231ed-aca0-5f43-8a7d-a6f09b72cc2e |  | 1 |
| f4ad8f66-812a-4d3f-967f-2372bf2faf6b | LOCATION | The repair workshop is Navjivan Motors Pvt. Ltd., an authorised Hyundai sales and services center. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | c65231ed-aca0-5f43-8a7d-a6f09b72cc2e, 8ae4bff9-02e8-594a-bde1-60156f25f484 |  | 1 |
| 94f17109-979d-40da-ab8b-4caa867fdb3c | CLAIM_DETAIL | The insurance company is Bajaj Allianz. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | 0fb92b74-8c4e-580f-aa01-6991d284ae02 |  | 1 |
| e5da41bb-cb55-4fe1-965a-951f56cac058 | PERSONAL_INFO | The customer name is Mahesh Khoei Vasava. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | b87ff850-bce1-5db7-9671-4fe3c78c1cab |  | 1 |
| 4adf2ff0-7ef4-4ea6-956a-abe4ab070cdc | VEHICLE_INFO | The vehicle color is White. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | 8ae4bff9-02e8-594a-bde1-60156f25f484 |  | 1 |
| 0ff9e2bf-2b8d-461f-9b03-17975af59b82 | VEHICLE_INFO | The vehicle model is EON. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | 8ae4bff9-02e8-594a-bde1-60156f25f484 |  | 1 |
| 482cad67-1411-4de5-8657-501fdb4a6952 | VEHICLE_INFO | The vehicle make is Hyundai. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | 8ae4bff9-02e8-594a-bde1-60156f25f484 |  | 1 |
| dba23968-6adc-4d84-bdb0-8d8c8bdb0f30 | VEHICLE_INFO | The vehicle registration number is GJ9924AA0436. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | 8ae4bff9-02e8-594a-bde1-60156f25f484 |  | 1 |
| c5d4d2b9-cbb6-43e4-9a41-8b3f8b3e25ab | DATE_TIME | The repair estimate date is 2023-08-09. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | 5dec1c3c-3916-5727-966d-8f059a56d791 |  | 1 |
| 422d3a15-fe9f-468f-a241-6452686045d1 | CLAIM_DETAIL | The repair estimate document number is 230. | 0.95 | 218890965_Repair_Estimate.jpg / 218890965_Repair_Estimate / repair_estimate | 029a72f8-7839-563a-b1f4-cfdf7bc87cf5 |  | 1 |
| 98aae3ec-4131-49c5-bcbc-1dbf3dcc52f4 | FINANCIAL | The total net premium is INR 5756.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy |  |  | 1 |
| 885fb8e1-8f2a-48e2-97dc-c7632c83c58a | FINANCIAL | The central GST at 9% is INR 518.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy |  |  | 1 |
| 4b0a7122-df8d-43f6-9e18-82bd6450483b | FINANCIAL | The final premium is INR 6792.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 0b5ba352-b1fd-53a1-96b8-536a75c61306 |  | 1 |
| 96b6d0bf-d1a3-4f9a-9d6e-fc0de72e9297 | DATE_TIME | The liability period is from 2023-08-03 to 2024-08-02. | 0.92 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 516f870e-b7af-5919-8e86-d734503c2df5, 21560b49-debb-5c2d-b869-04129a63d7f4, c45e5a8f-32ee-5330-aee1-ef0746cee69b |  | 2 |
| f49ad90d-44a9-4965-912c-1a27c4a06d43 | VEHICLE_INFO | The seating capacity is 5. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy |  |  | 0 |
| 9591051c-7ef0-4e92-8295-202fe9d2ac33 | VEHICLE_INFO | The year of vehicle manufacturing is 2013. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 0 |
| 5fb89f79-eae0-45a5-890f-ff33a75b9327 | CLAIM_DETAIL | The policy number is OG-24-2203-1801-00005412. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4, 8256265f-bda3-59c3-b052-5797d78ce904 |  | 1 |
| 781c4ab2-cc94-4184-b5a7-f89863a91f37 | PERSONAL_INFO | The insured name is MAHESHKUMAR INDRASING VASAVA. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 9359f38c-16bb-539a-9156-b5378f397d1b, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 370332e0-f81d-4a1d-9b6d-963d13e017ee | LOCATION | The insured address is 6 NANA VARACHHA HOUSING SOCIETY NANA VARACHHA DHAL, NANA VARACHHA, KAMREJ ROAD SURAT CITY, SURAT, GUJARAT-395006. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 8305f8ac-6233-542a-8abd-2fb5ce10804a, 7bad1733-bf8e-52d9-a67c-f5f174d27527, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 3572a04c-e89c-4f37-9ee4-5626344b8b5f | CLAIM_DETAIL | The customer ID is 399252385. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 39f5eece-6ff0-5880-84ca-65aabd996763, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 769b847d-ba90-4cf0-b118-348f56af9d3e | LOCATION | The place of supply is Gujarat (state code 24). | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 8305f8ac-6233-542a-8abd-2fb5ce10804a, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| a96b07ea-41b9-43ff-b115-83fb9a03e5df | DATE_TIME | The policy was issued on 2023-08-02 at 18:54. | 0.92 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4, 499a469e-98cb-5c03-b0ba-4529962faf1c |  | 1 |
| 661df07f-bd6d-48bb-af49-3940ea3df90c | DATE_TIME | The policy period starts on 2023-08-03 at 18:54. | 0.92 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4, c45e5a8f-32ee-5330-aee1-ef0746cee69b |  | 1 |
| 57fa8b22-497a-4578-b674-d3e6f729de0e | DATE_TIME | The policy period ends on 2024-08-02 at midnight. | 0.92 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 516f870e-b7af-5919-8e86-d734503c2df5, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| b2e9d509-a7fa-4da7-a1d3-9370801b5f33 | CLAIM_DETAIL | The invoice number is 588338246/1. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4, c381d22d-19ec-5718-ba78-05dfa9561971 |  | 1 |
| 174ea5da-bb56-4915-93c8-f2b65d1f2f6e | CLAIM_DETAIL | The company GST number is 24AABCB5730G1Z3. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | dac20136-ad6d-53a0-9e5e-cf8a693637d1, 21560b49-debb-5c2d-b869-04129a63d7f4, 37945fed-5adb-5b19-9881-6f69d0e08cb4 |  | 1 |
| 6b755373-05a5-4916-b558-3f3290d42cb4 | CLAIM_DETAIL | The company PAN is AABCB5730G. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | dac20136-ad6d-53a0-9e5e-cf8a693637d1, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 5c15ed05-5c81-4c51-83fb-98bbafcdd7c2 | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | f499d7f7-de0e-5d2f-a7e9-5778288d5b76, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 993e974b-bfab-4388-883f-db16f99b2727 | LOCATION | The place of vehicle registration is GJ27-AHMEDABAD. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| c192afaa-3354-4479-a27c-f6c03a1e13ac | VEHICLE_INFO | The engine number is G3HADM199755. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | f2ac6f6b-b0b6-57e0-a383-79984bbae18e, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 578cfdc0-670e-45ad-9934-dd2f1d1ab984 | VEHICLE_INFO | The chassis number is MALA351ALDM226944. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4, e4796257-98c5-57c6-a475-b7dc69136521 |  | 1 |
| 490ba3c6-5bbb-446c-966d-2fa17337d234 | VEHICLE_INFO | The vehicle make is HYUNDAI. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| e09bdfec-2245-45ab-ad9e-1a628a600f6f | VEHICLE_INFO | The vehicle model is EON. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 0c5f0c97-c6ff-4f3d-9887-cc310c118dfa | VEHICLE_INFO | The vehicle subtype is SPORTZ. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| cffefaac-c367-413a-9a58-5254d0e41338 | CLAIM_DETAIL | The no-claim bonus is 0%. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy |  |  | 0 |
| 96fec4fb-bbfd-4253-87eb-b24fad5a030a | VEHICLE_INFO | The engine capacity is 814 CC/KW. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy |  |  | 0 |
| 5518e6f6-747d-4aa5-bfdf-ce2c6ffeb1b4 | RELATIONSHIP | The vehicle is hypothecated to BAJAJ FINANCE LIMITED. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 553584ea-bc9d-5fd5-87e7-c47279f01fef, 2388f7f0-f036-5dd2-ab38-8164d19d4481 |  | 2 |
| 61cf4c9b-22cc-479f-b3a3-db8c9c1a0eb2 | CLAIM_DETAIL | The policy product type is PRIVATE CAR PACKAGE POLICY. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 0 |
| ab3de816-c876-495c-97e0-7b03ab7618d3 | LOCATION | The geographical area is India. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 8313375a-b218-4691-a22a-2a4ac66616a6 | LOCATION | The registered office is Bajaj Allianz House, Airport Road, Yeravada, Pune-411006, India. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 553584ea-bc9d-5fd5-87e7-c47279f01fef, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 2dd95ea0-a570-41f0-805e-d6c64297c807 | PERSONAL_INFO | The contact phone number for the policy issuing office is +919876256882. | 0.92 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 1768ed11-a4ad-5e58-ab00-823b13869952, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| e367e2c9-da6a-40cd-be0b-dae15645ce3d | LOCATION | The policy issuing office and correspondence address is 202, 2ND FLOOR, THE CITADEL, OPPOSITE STAR BAZAAR, ADAJAN, Surat-395009. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 7bad1733-bf8e-52d9-a67c-f5f174d27527 |  | 1 |
| b3644f8d-c709-47db-ab1e-eee9716ac9c7 | CLAIM_DETAIL | The IRDAI registration number is IRDAN113RP00251V01200102. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 8a3800b8-685c-5404-a06f-4a30c182806a, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 9de62908-995b-4e7f-a642-a6ef71042259 | CLAIM_DETAIL | The insurer is BAJAJ ALLIANZ GENERAL INSURANCE COMPANY LIMITED. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 4fd78460-e555-5e90-bef2-ff10dad05fe8 |  | 1 |
| 0508a76c-00af-4b06-816b-068060e9bd70 | FINANCIAL | The vehicle IDV is INR 200000.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | ac3a290c-0942-5945-af0c-0ee051c707f9, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 15924afa-4d72-49c8-ba4a-7797cfd324db | FINANCIAL | The own damage premium is INR 3031.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 180166a9-bdba-505a-aecd-331e648e679f, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 4b4c70ec-50a9-4c22-8eb8-501f2d8c2cb9 | FINANCIAL | The total OD premium is INR 3031.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 180166a9-bdba-505a-aecd-331e648e679f, 21560b49-debb-5c2d-b869-04129a63d7f4 |  | 1 |
| 4a0459ba-6c62-420b-9d13-cf76369e4286 | FINANCIAL | The basic third party liability premium is INR 2094.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 553584ea-bc9d-5fd5-87e7-c47279f01fef, 21560b49-debb-5c2d-b869-04129a63d7f4, 87cd1df7-766a-5416-8891-befd42a773a3 |  | 1 |
| 6b357019-3261-4068-8a6d-c01bdb915c04 | FINANCIAL | The PA cover for owner-driver with sum insured INR 1500000 has a premium of INR 331.00. | 0.92 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 553584ea-bc9d-5fd5-87e7-c47279f01fef |  | 2 |
| 1aea3259-0423-4d63-b885-9ce4a630b09a | FINANCIAL | The liability to person for paid driver/operation/maintenance premium is INR 50.00. | 0.92 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 553584ea-bc9d-5fd5-87e7-c47279f01fef |  | 1 |
| cabde65f-6fea-4dff-8432-dd88ffd867c7 | FINANCIAL | The PA cover for 5 passengers at INR 100000 each has a premium of INR 250.00. | 0.92 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy | 553584ea-bc9d-5fd5-87e7-c47279f01fef |  | 2 |
| 6d48527d-9a9b-4e17-ad67-c7a4c77928a6 | FINANCIAL | The total act premium (liability) is INR 2725.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy |  |  | 1 |
| 7a3b496b-b03c-4209-af7b-9166a8fc818e | FINANCIAL | The state GST at 9% is INR 518.00. | 0.95 | 218891028_Policy_Copy.jpg / 218891028_Policy_Copy / policy_copy |  |  | 1 |
| d18cd5d6-332e-4b9a-960a-b0b5a1bef6ca | CLAIM_DETAIL | The PAN card was issued by the Income Tax Department, Government of India. | 0.95 | 219032034_AML_Documents.jpg / 219032034_AML_Documents / pan_card | b4790284-da4f-5720-a039-71157369460f, 03f94ffb-4c01-553a-9af9-e698b668c808, a66a986f-a5e4-50a8-bd89-bf018b8c9557 |  | 1 |
| 32854170-d7b6-44ce-8e8c-28f50336e094 | PERSONAL_INFO | A handwritten signature is present on the PAN card. | 0.95 | 219032034_AML_Documents.jpg / 219032034_AML_Documents / pan_card | b4790284-da4f-5720-a039-71157369460f, a66a986f-a5e4-50a8-bd89-bf018b8c9557 |  | 0 |
| 0f226ebd-4139-4297-a05b-90db9e1b95cd | CLAIM_DETAIL | A QR code is present in the upper right corner of the PAN card. | 0.95 | 219032034_AML_Documents.jpg / 219032034_AML_Documents / pan_card | ecacd7ff-c41b-569d-a681-472d166be33a, a66a986f-a5e4-50a8-bd89-bf018b8c9557 |  | 0 |
| 157da8c8-389c-4dd6-8a93-9b3169fe5b0a | CLAIM_DETAIL | The PAN card displays the Ashoka Emblem with 'GOVT OF INDIA' text. | 0.95 | 219032034_AML_Documents.jpg / 219032034_AML_Documents / pan_card | ecacd7ff-c41b-569d-a681-472d166be33a, a66a986f-a5e4-50a8-bd89-bf018b8c9557 |  | 0 |
| cf7063a9-6919-4e57-b7b6-ae81a27839f1 | CLAIM_DETAIL | The PAN number is BOTPV1228N. | 0.95 | 219032034_AML_Documents.jpg / 219032034_AML_Documents / pan_card | 54aded9a-4ef0-5a68-ae8c-1d556b787065, b4790284-da4f-5720-a039-71157369460f |  | 1 |
| 92ecd3c1-cbc1-4247-91df-cb2649f8d345 | PERSONAL_INFO | The PAN cardholder name is BHRIKUMAR INDRASING VASAVA. | 0.95 | 219032034_AML_Documents.jpg / 219032034_AML_Documents / pan_card | b4790284-da4f-5720-a039-71157369460f, 8af252d8-fc7a-523c-abbe-008e8485f499, a66a986f-a5e4-50a8-bd89-bf018b8c9557 |  | 1 |
| d3c562b4-83b7-454e-9718-42ab0afb5971 | PERSONAL_INFO | The father's name is INDRASING DIVEJIYABHAI VASAVA. | 0.95 | 219032034_AML_Documents.jpg / 219032034_AML_Documents / pan_card | c62b6bb7-b8cd-56f9-bea8-73ff4ab07678, b4790284-da4f-5720-a039-71157369460f |  | 1 |
| cfd1d779-db4d-4efe-ba01-829e552ac6e1 | CLAIM_DETAIL | Police Panchanama or FIR is required for accident claim settlement in case of Third Party property damage, Death, or Body Injury. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| 93049867-b688-436f-8d9b-fc0d50b73a31 | CLAIM_DETAIL | Repair bills and payment receipts after job completion are required for accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| ab721408-e8e9-4d1d-965b-3a1f6c4ab9c4 | CLAIM_DETAIL | AML and KYC documents as per guidelines are required for accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| f4b4d58a-cb90-498f-b72f-83ea3188d52c | CLAIM_DETAIL | A Claims Discharge Cum Satisfaction Voucher signed across a Revenue Stamp is required for accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| 40a47bde-d5b3-4d02-afcc-01704b5b179e | CLAIM_DETAIL | Additional documents are required for commercial vehicle accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| 0130338c-9227-4e22-9454-81845b3a05fe | CLAIM_DETAIL | Permit, Fitness, and Load Challan are required for commercial vehicle accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| f18af0b9-d0b6-4cd2-a75c-693476658607 | CLAIM_DETAIL | Documents must be submitted to the nearby Bajaj Allianz Office for claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 1 |
| 9af006ef-c676-4c7a-aa0d-b78ab9c9a00a | CLAIM_DETAIL | A duly filled and signed claim form is required for accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| a98379b2-9b5f-4c3f-8e2f-5f27d3f9314b | CLAIM_DETAIL | Proof of insurance policy or covermote copy is required for accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| c14bde88-fd5c-47de-bca9-f58cbba274ca | CLAIM_DETAIL | A copy of the Registration Book and Tax Receipt is required for accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| 6f092e4f-182d-44b3-a2e8-88509ac60e40 | CLAIM_DETAIL | A copy of the Motor Driving Licence of the person driving the vehicle at the material time is required for accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| 24658bee-5eb8-4455-af36-5bc4bac16837 | CLAIM_DETAIL | An estimate for repairs from the repairer is required for accident claim settlement. | 0.95 | 219032051_Claim_Form.jpg / 219032051_Claim_Form / correspondence |  |  | 0 |
| f67bb30f-845b-47c9-8264-553fa911b757 | CLAIM_DETAIL | The gate pass serial number is 1800. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | fe047750-2680-549b-b408-b58b0e3f7d0f, efd36176-272d-58db-bdbc-391c3dea7755 |  | 1 |
| 71e5b003-bfb5-478c-ad5f-623d31ef53f7 | DATE_TIME | The vehicle check-in time was 10:45 PM. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 8454ee1b-0fa3-5c86-a262-fe7aa243629d, efd36176-272d-58db-bdbc-391c3dea7755 |  | 1 |
| a9d93eb6-a0ad-49cb-afa4-a8ee888074d6 | LOCATION | Navjivan Motors Pvt. Ltd. is an authorized Hyundai sales and services center. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 1bbe2ce2-9359-5aa7-98f1-d21aa3b4746a, 8fb25af8-d434-59b1-bdf7-288aec56ef5d |  | 1 |
| 580a5809-f2af-4a78-8a2d-d80e03cf3699 | LOCATION | Navjivan Motors Pvt. Ltd. is located in Surat near SMC Ultima South Zone Office, Devchand Nagar. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 1bbe2ce2-9359-5aa7-98f1-d21aa3b4746a, e3d062ac-3b4e-5db8-9928-eea3f7e10cf4, 8fb25af8-d434-59b1-bdf7-288aec56ef5d |  | 2 |
| a4f5346f-7fcf-4040-8e5e-d312ef979c95 | VEHICLE_INFO | The vehicle odometer reading at time of exit was 219213 kilometers. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | efd36176-272d-58db-bdbc-391c3dea7755, 6c6911be-b180-5dbb-8e88-c874cb836b6f, 465d5717-b929-5a90-a4a8-47945b1b586e |  | 1 |
| 2d48992c-1f2d-499e-a285-06572d87aae3 | LOCATION | Navjivan Motors Pvt. Ltd. contact phone numbers are 263 1000, 263 2000, and 263 3000. | 0.90 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 1bbe2ce2-9359-5aa7-98f1-d21aa3b4746a, 99fca8fc-ffbf-5731-a32b-3a3a3f7f23ac, efd36176-272d-58db-bdbc-391c3dea7755 (+1 more) |  | 1 |
| 8f66a606-243a-431e-a329-d0863dc0de23 | LOCATION | Navjivan Motors Pvt. Ltd. fax number is 263 1010. | 0.90 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 1bbe2ce2-9359-5aa7-98f1-d21aa3b4746a, 8fb25af8-d434-59b1-bdf7-288aec56ef5d |  | 1 |
| 9919e3b7-2852-4d52-820e-2f9cad573af5 | LOCATION | Navjivan Motors Pvt. Ltd. email address is navjivanmotors@gmail.com. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 1bbe2ce2-9359-5aa7-98f1-d21aa3b4746a, 8fb25af8-d434-59b1-bdf7-288aec56ef5d |  | 2 |
| 4bd9321b-8a85-42ec-9819-5e5a9c2ee11c | VEHICLE_INFO | The vehicle registration number is GH27AA0136. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | efd36176-272d-58db-bdbc-391c3dea7755, 465d5717-b929-5a90-a4a8-47945b1b586e |  | 1 |
| 77106c9b-b662-4a38-857b-56473c3dff2c | RELATIONSHIP | Nana Varaziha accompanied Vikesh Patil. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 50d76286-cd6f-5c8c-8c97-177a4a0b8c85, efd36176-272d-58db-bdbc-391c3dea7755, 540352f1-699b-5a08-a6bb-143e7835263d |  | 2 |
| 960846cb-2299-4998-9245-837a23aa4cda | DATE_TIME | The gate pass was issued on 2023-08-09. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | efd36176-272d-58db-bdbc-391c3dea7755, cb95a01a-9cae-5d0c-ae14-d615bdb7c30d |  | 1 |
| e421b101-59f9-4fe5-b9d1-e6d6ae5f7ed5 | FINANCIAL | The gate pass amount is INR 2000. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 99fca8fc-ffbf-5731-a32b-3a3a3f7f23ac, efd36176-272d-58db-bdbc-391c3dea7755 |  | 1 |
| edae9fcf-a65e-47e3-a42b-b038a2c0189f | PERSONAL_INFO | Vikesh Patil is authorized to exit the premises. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | efd36176-272d-58db-bdbc-391c3dea7755, 540352f1-699b-5a08-a6bb-143e7835263d |  | 1 |
| 612036f4-1fea-464c-b430-ccff02f89dd7 | PERSONAL_INFO | Vikesh Patil's phone number is +919727635980. | 0.95 | 219032145_Job_Card.jpg / 219032145_Job_Card / payment_slip | 9765aed9-958f-5044-b324-ef3db07939c5, efd36176-272d-58db-bdbc-391c3dea7755, 540352f1-699b-5a08-a6bb-143e7835263d |  | 2 |
| 0550e72b-d443-4a73-8312-c58e11129e49 | CLAIM_DETAIL | The insurance company is Bajaj Allianz General Insurance Company Limited. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 2de91c2b-bdd0-57e4-934a-5e30177a9e7a, 02f9d008-e4b6-5842-8138-eac801ca1ccb |  | 1 |
| ee8f96cd-2612-48d2-8226-286bc7331b19 | CLAIM_DETAIL | The repair estimate number is ET23080090. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | e71dc912-d4d4-5208-bd52-026e499babd1 |  | 1 |
| d5bfa77c-1d8b-4e31-a0fe-30e2618b9837 | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | df4f449d-eb19-517a-9547-f997a542f2e1, b50c1b67-d7bc-5b78-91ac-71a40ec1ea4c |  | 1 |
| f110af1d-b00a-4404-94b2-4a44ec091bb7 | VEHICLE_INFO | The vehicle model is EON. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | df4f449d-eb19-517a-9547-f997a542f2e1 |  | 1 |
| 001fdb9f-2781-4d27-90cf-6c682264eee4 | VEHICLE_INFO | The vehicle chassis number is MALA351ALDM226944. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 85620315-cf2a-5545-b402-8e43dba6c811, df4f449d-eb19-517a-9547-f997a542f2e1 |  | 1 |
| b44e4528-bf23-4cd3-a381-598a25fdfe69 | VEHICLE_INFO | The vehicle engine number is G3HADM199755. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | e10404df-a550-5495-a4ea-b792b110a7f5, df4f449d-eb19-517a-9547-f997a542f2e1 |  | 1 |
| 737e366b-446f-4f21-a603-67598676eb0e | VEHICLE_INFO | The vehicle color is C.White. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | df4f449d-eb19-517a-9547-f997a542f2e1 |  | 1 |
| 03eda4cb-92c9-4d03-93d3-844568ecfc96 | DATE_TIME | The repair estimate date is 2023-08-16. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate |  |  | 1 |
| 15f9ea94-86b8-48f0-8276-4357cacf65be | CLAIM_DETAIL | The claim number is R202305933. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | da35a6d3-5b3a-5edb-8dbb-d4cee880e790, 2de91c2b-bdd0-57e4-934a-5e30177a9e7a |  | 1 |
| 45266045-16ce-4903-84c4-3d77e0e66282 | INCIDENT | The work type is Accidental Repair. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate |  |  | 1 |
| 493aea34-dda8-4d46-873f-a261848b3059 | PERSONAL_INFO | The customer name is MAHESHKUMAR INDRASING VASAVA. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | f48d953a-860c-5a4f-896b-e288eb0715e7, 3c479128-7c7d-59cc-944b-1ef7de5ba245 |  | 1 |
| b502c2db-bb9a-4fc5-919e-4678282a34f7 | LOCATION | The customer address is 6 NANA VARACHHA HOUSING SOC.DHAL NANA VARACHHA KAMREJ SURAT. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | f48d953a-860c-5a4f-896b-e288eb0715e7 |  | 1 |
| effb2f1a-6165-4d04-b9cc-c6d79c16578a | CLAIM_DETAIL | The workshop name is M/S NAVJIVAN MOTORS PVT.LTD. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | fcde1f08-f462-5b6b-ae41-91fb4411d169, 9831b8dd-6c0c-53e0-86f3-bb0807124a5b |  | 1 |
| 2113839c-bd9d-4f08-8040-f3e81e01498d | FINANCIAL | The total repair estimate amount is INR 112712.22. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 132ffb4a-6efa-5cc0-838c-ad668037facf, 0b038f4b-8c96-5d49-b177-a4b691295937 |  | 1 |
| 57f71856-fa46-44de-8524-1a037d4f367c | FINANCIAL | The total parts amount is INR 47612.80. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | b5486c6a-c357-57a7-93db-1be4716e316c, 132ffb4a-6efa-5cc0-838c-ad668037facf |  | 1 |
| 6c70215f-ac33-4fa5-b3dd-c2f8f0172354 | FINANCIAL | The total labour amount is INR 65099.42. | 0.95 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 132ffb4a-6efa-5cc0-838c-ad668037facf |  | 1 |
| 6b2a0d6c-0656-410d-b760-faaeb1ff5ea2 | FINANCIAL | The repair estimate includes a sealant kit for windshield glass (part number 08M9886100) at INR 1024.03. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8fe14333-2166-5d49-8460-e9346c4581b7, 8a2558d3-1afd-52ff-8b63-27e11316d3c0 |  | 2 |
| be53cd83-d714-408a-8f4b-f9b4b528133d | FINANCIAL | The repair estimate includes a radiator assembly (part number 253104N000) at INR 2602.07. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8fe14333-2166-5d49-8460-e9346c4581b7, 8a2558d3-1afd-52ff-8b63-27e11316d3c0 |  | 2 |
| d517ce67-7f5e-41af-bd37-4cb49c105752 | FINANCIAL | The repair estimate includes a front drive shaft assembly (part number 495004N000) at INR 6099.23. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8a2558d3-1afd-52ff-8b63-27e11316d3c0 |  | 2 |
| a64d0fbe-1e72-4b84-b1f8-3a1b28eedda2 | FINANCIAL | The repair estimate includes a windshield glass (part number 8611105200) at INR 4939.30. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8fe14333-2166-5d49-8460-e9346c4581b7, 8a2558d3-1afd-52ff-8b63-27e11316d3c0 |  | 2 |
| dfcf5927-1a27-40d5-ae85-4aca0d50aebb | FINANCIAL | The repair estimate includes a compressor assembly (part number 977014N100) at INR 10666.14. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8a2558d3-1afd-52ff-8b63-27e11316d3c0 |  | 2 |
| 2e8f7311-130b-4682-98d2-ed28ba13a637 | FINANCIAL | The repair estimate includes labour for radiator assembly at INR 944.00. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8fe14333-2166-5d49-8460-e9346c4581b7, 8a2558d3-1afd-52ff-8b63-27e11316d3c0 |  | 1 |
| 36061bfe-5e80-4de5-a52a-ceb2f388386a | FINANCIAL | The repair estimate includes labour for windshield glass installation at INR 1888.00. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8fe14333-2166-5d49-8460-e9346c4581b7, 8a2558d3-1afd-52ff-8b63-27e11316d3c0 |  | 1 |
| 47010556-c197-4545-8f5b-f4cabb853e8f | FINANCIAL | The repair estimate includes denting and repairing charges at INR 17700.00. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8fe14333-2166-5d49-8460-e9346c4581b7 |  | 1 |
| 7fec3bd9-c7b9-44de-b5ae-8b3366fe6667 | FINANCIAL | The repair estimate includes painting charges at INR 31860.00. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8fe14333-2166-5d49-8460-e9346c4581b7 |  | 1 |
| c57942cd-9a0b-497a-a09b-8fda58b9b4fd | FINANCIAL | The repair estimate includes vehicle towing charges at INR 1498.60. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate | 8fe14333-2166-5d49-8460-e9346c4581b7 |  | 1 |
| bd873085-6952-431b-a7fa-7bbeefc44000 | DATE_TIME | The repair estimate document was printed on 2023-08-16 at 18:05. | 0.92 | 219358654_Repair_Estimate.pdf / 219358654_Repair_Estimate / repair_estimate |  |  | 1 |
| b76e2b66-d521-40d1-8ebe-5f9aba0f0c02 | VEHICLE_INFO | The vehicle color is WHITE. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | 50b3e6b5-3bfe-5738-9b19-b4290ffe4633, b45318d2-c0f8-5fca-8587-5b2b11629411 |  | 1 |
| 55ea503a-6347-4f94-83f3-9f9f952b0540 | VEHICLE_INFO | The vehicle make is HYUNDAI. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | 8a09c1e0-7219-53a9-8841-59ccc0a16c95, b45318d2-c0f8-5fca-8587-5b2b11629411 |  | 1 |
| c3ccee49-759f-49f7-965e-f3e0d51a0190 | VEHICLE_INFO | The vehicle engine number is G3JH0M199756. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | c7b6323b-12cc-5e06-8473-a8acae3c7e26, b45318d2-c0f8-5fca-8587-5b2b11629411 |  | 1 |
| 5a8f4682-d1a4-4e40-b3fe-24ad731f4a77 | VEHICLE_INFO | The vehicle chassis number is MALA351AL0R226944. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | b45318d2-c0f8-5fca-8587-5b2b11629411, 88bbfe1c-7017-51ec-8236-9d75c5334d2f |  | 1 |
| 1a8d408c-d9b8-4fcc-bd43-608c764d0159 | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | 786969f6-cc4d-55d7-a68d-681539a78d32, b45318d2-c0f8-5fca-8587-5b2b11629411 |  | 1 |
| 4180c352-786d-4ba5-b3d8-4e1e0193bc7b | VEHICLE_INFO | The vehicle class is LMV (CAR). | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | 50b3e6b5-3bfe-5738-9b19-b4290ffe4633, ced8ffe6-5d6f-5997-92a3-6a0346d12578 |  | 1 |
| 27af71b2-406f-4d5c-b7ef-f2adb1bd4e0f | VEHICLE_INFO | The vehicle fuel type is PETROL. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | 50b3e6b5-3bfe-5738-9b19-b4290ffe4633, b45318d2-c0f8-5fca-8587-5b2b11629411 |  | 1 |
| ee41dc54-16bb-4619-b874-bd2d2eaf271c | DATE_TIME | The registration certificate was issued on 2013-10-17. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | 6d457fdb-2df6-5f55-acf0-ec71b78510db, ced8ffe6-5d6f-5997-92a3-6a0346d12578 |  | 1 |
| f41e7ce3-efa9-4ecd-b2e4-6a8b63d3cca2 | VEHICLE_INFO | The vehicle cylinder capacity is 1197 CC. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | b45318d2-c0f8-5fca-8587-5b2b11629411, 187d3635-72a9-5339-ab22-d269465e6d74 |  | 1 |
| d054f395-d4d4-47c2-abc8-f3bdf388d5a5 | DATE_TIME | The registration certificate validity expires on 2028-10-16. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | ced8ffe6-5d6f-5997-92a3-6a0346d12578, 5f42d811-82b3-549d-98b2-387d5cbb1f8a |  | 1 |
| 61b810db-6d1e-4091-84dc-6848e3591072 | VEHICLE_INFO | The hypothecation status is NIL. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | 50b3e6b5-3bfe-5738-9b19-b4290ffe4633, ced8ffe6-5d6f-5997-92a3-6a0346d12578 |  | 1 |
| 60d84a30-3574-4055-9be3-24336519d043 | VEHICLE_INFO | The registration authority is Government of Gujarat. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | a8fe30df-66c1-5906-b98f-e3fc87e4215b, ced8ffe6-5d6f-5997-92a3-6a0346d12578 |  | 1 |
| d9b13a1c-e377-4bfa-9513-c32ee5b6c000 | VEHICLE_INFO | The vehicle model is i10 SPORT 2 BWM. | 0.95 | 219430367_Pre_Inspection_Photographs_Reports.PDF / 219430367_Pre_Inspection_Photographs_Reports / vehicle_document | b45318d2-c0f8-5fca-8587-5b2b11629411 |  | 1 |
| d1a5d7b6-2f8f-4aef-bb25-947a0a08d730 | CLAIM_DETAIL | A reference number 9474625160 is present in the document. | 0.85 | 222633146_Statement_of_Insured.pdf / 222633146_Statement_of_Insured / insured_statement | 0b4ec0ef-d9ba-56b4-bf52-938f635dc79c, 06fa02ae-94ed-5030-ae26-1ad745469312 |  | 1 |
| cf9ea55c-4243-4e3c-a6a8-05359e651761 | PERSONAL_INFO | A phone number 9411411 is associated with the insured statement. | 0.50 | 222633146_Statement_of_Insured.pdf / 222633146_Statement_of_Insured / insured_statement | 320cba5f-55f5-5ae5-9040-d3717a4fa833, e36f046f-8e44-55f2-855b-a6820d59eafb |  | 1 |
| 1d5a26d1-68d2-4ab1-b6e2-492caf686523 | PERSONAL_INFO | Prasann Maheshwari is the signatory of this insured statement. | 0.95 | 222633146_Statement_of_Insured.pdf / 222633146_Statement_of_Insured / insured_statement | f8eb2cbf-77a3-509a-89d6-869fee95bb96, 0b4ec0ef-d9ba-56b4-bf52-938f635dc79c |  | 1 |
| 2d3e5925-fe90-43ea-94dc-504147bb5ad6 | DATE_TIME | The insured statement was dated 2023-09-19. | 0.95 | 222633146_Statement_of_Insured.pdf / 222633146_Statement_of_Insured / insured_statement | 320cba5f-55f5-5ae5-9040-d3717a4fa833, d7a4eeb6-3459-5c6f-9d1e-b5261140dd24 |  | 1 |
| 83f53c1d-d6cf-4af6-acbf-82096e08d6bd | CLAIM_DETAIL | The document is a handwritten insured statement in Gujarati language. | 0.95 | 222633146_Statement_of_Insured.pdf / 222633146_Statement_of_Insured / insured_statement | 3d2e333a-58b8-5fbc-9f46-8a8822b020b2, 4ee35290-8e00-543b-932b-80258c409674, 70922374-5b42-58a1-b85f-d93c3715d6e8 |  | 0 |
| ff85539b-ab59-401e-a8cd-1d403af6e008 | CLAIM_DETAIL | The insured statement contains a handwritten signature at the bottom. | 0.95 | 222633146_Statement_of_Insured.pdf / 222633146_Statement_of_Insured / insured_statement | 320cba5f-55f5-5ae5-9040-d3717a4fa833 |  | 0 |
| 0a87b007-e5df-48a4-a943-770fb4575e3c | INCIDENT | The document contains a handwritten narrative in Gujarati script describing the incident. | 0.85 | 222633187_Statement_of_Driver.pdf / 222633187_Statement_of_Driver / driver_statement | 4fb7ef04-aa4c-5dc1-ac2a-ef586101a04e, 1549c5d8-4c98-5b53-b023-929f2eca44b1 |  | 0 |
| 0d71ef46-170e-4392-9a58-2af94607b31f | PERSONAL_INFO | The contact phone number is +918308953545. | 0.95 | 222633187_Statement_of_Driver.pdf / 222633187_Statement_of_Driver / driver_statement | 4fb7ef04-aa4c-5dc1-ac2a-ef586101a04e, 77aa8e68-3bb8-5444-bbbf-723e2f8550b7, 523a30dd-0e52-5ecc-b0ce-9d03640ca963 |  | 1 |
| a49e9ea0-2fd9-4d2b-aaa0-65211f264d3e | DATE_TIME | The incident date is 2023-08-19. | 0.95 | 222633187_Statement_of_Driver.pdf / 222633187_Statement_of_Driver / driver_statement | 4fb7ef04-aa4c-5dc1-ac2a-ef586101a04e, 77aa8e68-3bb8-5444-bbbf-723e2f8550b7, 1f31f434-2524-5c78-889c-b0a33cb25143 |  | 1 |
| d4083ebe-0366-49be-aecb-1ddda4bb5f95 | DATE_TIME | The document date is 2023-08-19. | 0.95 | 222633187_Statement_of_Driver.pdf / 222633187_Statement_of_Driver / driver_statement | 4fb7ef04-aa4c-5dc1-ac2a-ef586101a04e, 77aa8e68-3bb8-5444-bbbf-723e2f8550b7, 1f31f434-2524-5c78-889c-b0a33cb25143 |  | 1 |
| 827a968a-4283-45d8-b355-017d3b124247 | CLAIM_DETAIL | The document language is Gujarati. | 0.95 | 222633187_Statement_of_Driver.pdf / 222633187_Statement_of_Driver / driver_statement | 1549c5d8-4c98-5b53-b023-929f2eca44b1 |  | 0 |
| dc0cfaed-82ec-49e1-8a9a-27350195c4ff | INCIDENT | The driver's signature is present at the bottom of page 2. | 0.90 | 222633187_Statement_of_Driver.pdf / 222633187_Statement_of_Driver / driver_statement | 4fb7ef04-aa4c-5dc1-ac2a-ef586101a04e |  | 0 |
| 8571648d-5867-46fe-8c20-608ee87d776f | INCIDENT | The vehicle headlights are damaged. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 712d0d1c-e04d-5596-ac2d-5a9403d13244 |  | 1 |
| afc3541a-61c5-44df-afc6-cf904d69c4fd | INCIDENT | The vehicle has severe front-end collision damage. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 712d0d1c-e04d-5596-ac2d-5a9403d13244, 8e2dcfd9-6163-5cb4-9a33-5621526aa309 |  | 2 |
| cbab403c-6670-4c81-a293-c1bec5f048d9 | VEHICLE_INFO | The vehicle is a white Hyundai i10 hatchback. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 4d863c29-21e9-52f0-8d81-9c50355a2c27, 4b25eb38-fec7-59f7-b330-e18d1289339d, 8e2dcfd9-6163-5cb4-9a33-5621526aa309 |  | 2 |
| 87a65f2e-66aa-4818-9f65-c0425bc5dd6a | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 00d6a426-e088-5b9d-b94f-f3984c19692d, bad749ef-5656-57a8-84af-804bca0de746, 8e2dcfd9-6163-5cb4-9a33-5621526aa309 |  | 1 |
| 2a7da89d-be4d-4def-b865-73b054cc01c7 | INCIDENT | Nine photographs document the vehicle damage from multiple angles. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | ba538023-79f8-56bb-b12d-86852fdffdd4 |  | 1 |
| c90617bd-82a3-40a7-b942-b781920220d9 | VEHICLE_INFO | The vehicle is registered in Gujarat. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 00d6a426-e088-5b9d-b94f-f3984c19692d, bad749ef-5656-57a8-84af-804bca0de746, a6972268-e784-5983-b64c-f7f18b08614e (+1 more) |  | 2 |
| 5e5a39b1-d8b8-4464-bb5d-911974461b74 | LOCATION | The vehicle is parked in a parking lot with other vehicles visible. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | ba538023-79f8-56bb-b12d-86852fdffdd4 |  | 2 |
| fb0e9bf9-538d-42b3-bd7e-9b5119f48ea8 | INCIDENT | Red tape in an X-pattern is visible across the vehicle hood. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 712d0d1c-e04d-5596-ac2d-5a9403d13244 |  | 1 |
| 711d4ec6-d2d3-4b0f-b0d5-14b7defa281c | INCIDENT | The vehicle front-left door shows impact damage. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 712d0d1c-e04d-5596-ac2d-5a9403d13244 |  | 1 |
| aeb75313-95f7-4de4-9b8d-009f3cf09716 | INCIDENT | The vehicle front-left fender shows impact damage. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 712d0d1c-e04d-5596-ac2d-5a9403d13244 |  | 1 |
| 06c16b95-0ec2-44eb-a87c-b42c5b4694cf | INCIDENT | The vehicle front bumper area is affected by impact damage. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 712d0d1c-e04d-5596-ac2d-5a9403d13244 |  | 1 |
| c17fd192-9e5c-4554-96de-855a5339f601 | INCIDENT | The vehicle hood is severely crushed and crumpled. | 0.95 | 222633313_Vehicle_Damage_Photo.pdf / 222633313_Vehicle_Damage_Photo / photograph | 712d0d1c-e04d-5596-ac2d-5a9403d13244, 8e2dcfd9-6163-5cb4-9a33-5621526aa309 |  | 1 |
| ac9d1688-21f2-4d2e-86ea-6294782671d8 | INCIDENT | Graffiti art on bridge structures is visible in the photographs. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| 7ec83d08-5171-423c-bac6-75df3b98dbb8 | LOCATION | The photograph collection documents street scenes in Surat, India. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7, 51a731c2-0c47-5921-b7ed-3286afbe8031, 5411a0c9-b60c-51b1-b1d4-b72057e54ac4 |  | 1 |
| 5a13122b-b7eb-41f6-ae84-15b12141060e | INCIDENT | An Unacademy branded auto-rickshaw is visible in the street scene. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7, 51a731c2-0c47-5921-b7ed-3286afbe8031, 203a4adf-7bf4-546a-8510-46cea9479e3d |  | 2 |
| 8853729e-d233-4002-abad-0c1fe5c9a609 | INCIDENT | The photograph collection contains 10 images of street scenes. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| 0c2b0caf-8fee-49e7-991c-3dd7fff5a361 | INCIDENT | The weather conditions in the photographs are predominantly overcast or cloudy. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| a7255756-6c53-4f3c-9984-573c73e02fb5 | INCIDENT | Auto-rickshaws in yellow and black, and green colored vehicles are visible in the street scenes. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 1 |
| 97373e6e-874d-476b-94a6-edc96ceaedd9 | INCIDENT | Motorcycles and scooters are visible in the street scenes. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 1 |
| 39def64e-5b01-403a-8487-28e4f7cbd2b9 | LOCATION | Overhead bridges and underpasses are visible infrastructure in the photographs. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| 382a3fe2-d68d-489d-996c-bb24e69e8ce0 | INCIDENT | Street-level shops and commercial establishments are visible in the photographs. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| 11d34ced-c2d4-440b-b5f8-2b2538500c7f | INCIDENT | Fruit and vegetable vendors are visible in the street scenes. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| 69b7b6fe-7883-49dc-b398-2bbc71c36bd6 | INCIDENT | Food cart vendors are visible in the street scenes. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| 1661240e-00eb-4d76-b38a-98cd60d97367 | INCIDENT | Shop signs in Hindi and Gujarati script are visible in the photographs. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| d0b113e7-ddf8-4e29-9add-17bc6023cb0b | LOCATION | Mature trees and vegetation are visible in the street scenes. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| 9cabbb48-0b74-4cb0-9fe1-ee89ea5df922 | LOCATION | Concrete buildings are visible in the street scenes. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| f2ea05fc-e135-457a-a0eb-e142f71565a4 | LOCATION | Boundary walls are visible infrastructure in the photographs. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| 629cf76d-02dc-4778-b79b-c1da720e5d39 | LOCATION | Paved roads are visible in the street scenes. | 0.95 | 222633407_Spot_Photo_Sketch.pdf / 222633407_Spot_Photo_Sketch / photograph | 814d97c0-d4f2-5497-9265-64a2df16d2e7 |  | 0 |
| d8ce762c-1293-4c41-a0c4-c359a7050ec4 | LOCATION | Bupusiraum Cabs is a vehicle dealership with the tagline 'Drive your dreams'. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | ef94d58b-ae4c-519f-931b-f7ed74ff522d, ad3f340a-7c34-572c-93a2-85694fdbecf1 |  | 1 |
| d7d3c59c-f105-48b4-815c-d72a8a64d551 | FINANCIAL | A fuel amount of INR 1510652 is listed on the vehicle purchase form. | 0.85 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | e06f85a7-8c5d-5a73-b79c-a4d40754d09a, f0591228-62d3-5a0e-ac89-4ff39ca3efad |  | 1 |
| d12a659b-dc2b-4730-8d0b-3e34b43e6eec | FINANCIAL | An amount of INR 149000 is listed as 'Badi' on the vehicle purchase form. | 0.80 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | f0591228-62d3-5a0e-ac89-4ff39ca3efad, 50b2ea3f-6af7-5258-9e09-2ba1e337e573 |  | 1 |
| 1137ab4d-f4e7-4543-912e-4a75473d2755 | VEHICLE_INFO | The vehicle registration number is 9227463964. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | edf79e0c-9c0b-5802-ac76-5d4a0f818b3b, 483da377-4754-5d23-a214-6de83e085427 |  | 1 |
| feb90b9e-38fe-4f8e-bc8d-a2b4d5c4d539 | PERSONAL_INFO | Bupusiraum Cabs has contact phone number +919913316746. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | ef94d58b-ae4c-519f-931b-f7ed74ff522d, 20ab0030-80ac-5615-a5d1-96ad7bfdefb4, ad3f340a-7c34-572c-93a2-85694fdbecf1 |  | 2 |
| a0ae164f-257f-457d-8e20-b4a17fd3892c | PERSONAL_INFO | Bupusiraum Cabs has contact phone number +919079385368. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | 42346f7b-d5b3-5e84-93b2-757aa5085e1a, ef94d58b-ae4c-519f-931b-f7ed74ff522d, ad3f340a-7c34-572c-93a2-85694fdbecf1 |  | 2 |
| e6a78bc6-ef3d-456e-9096-80628161f218 | PERSONAL_INFO | Mahesh Vasava is associated with the email address mivasava1988@gmail.com. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | 1562109d-0668-5b60-816e-2c0ec6308f40, 3780c361-59a9-5d12-8bdb-d5d98ade123c |  | 2 |
| 9b7daac3-9f7b-4f35-ab65-9015e23a5c23 | PERSONAL_INFO | Prakash Chaudhari is associated with the email address uahachaudhari28@gmail.com. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | d89ebad8-d87f-586c-aae3-b7c6b2eeae9f, 8092259a-efdc-5741-bddb-23e852334387 |  | 2 |
| 74d5efe6-4e24-41cf-8c5e-59d6235bdc3c | DATE_TIME | Google Maps Timeline records show access to August 19, 2023. | 0.90 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | 968fe606-e8ca-5561-afcc-b57d78e05f86 |  | 1 |
| eece335b-0e0b-4a73-9cb3-6d0b3328402c | DATE_TIME | A vehicle photograph is associated with the location 'Candu Uka' and timestamped August 3 at 3:47 PM. | 0.85 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | 6ce4e804-599f-5cfc-9e8b-f7d3b2343287 |  | 2 |
| 9a4cfdde-ccca-4340-892a-c50004ce8e98 | FINANCIAL | A commission amount of INR 29950 is listed on the vehicle purchase form. | 0.85 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | f0591228-62d3-5a0e-ac89-4ff39ca3efad, 8e529827-09bd-5efe-827e-907c46a0740c |  | 1 |
| 666af635-ddcd-405f-a7d8-53bdede1fe11 | FINANCIAL | A depreciation amount of INR 1510664 is listed on the vehicle purchase form. | 0.85 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | 79e869fa-a369-5f53-99a6-4775834adf97, f0591228-62d3-5a0e-ac89-4ff39ca3efad |  | 1 |
| caad03b9-efb0-4813-8456-3b93f4f0bb02 | VEHICLE_INFO | The vehicle odometer reading is 500012/01. | 0.90 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | a82e6ac2-5f51-5127-8269-c6e97eceb9d7, edf79e0c-9c0b-5802-ac76-5d4a0f818b3b |  | 1 |
| ebd5ceff-874a-4cef-8330-830f7741e816 | VEHICLE_INFO | The vehicle registration number on the purchase form is 9455504. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | f0591228-62d3-5a0e-ac89-4ff39ca3efad, f7aa5b21-44a6-5c5f-b03b-73b0574b2c16 |  | 1 |
| 768da60e-2c79-4465-9099-a15563938dc7 | DATE_TIME | The vehicle purchase form is dated 2023-07-27. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | f0591228-62d3-5a0e-ac89-4ff39ca3efad, 258bbbc1-3e42-5dae-9a6f-9388da182ebb |  | 1 |
| 35e86c0f-8591-4e6b-8d38-a1250c6ab93d | VEHICLE_INFO | The vehicle model year is 2011. | 0.95 | 222633435_Any_Other.pdf / 222633435_Any_Other / other | edf79e0c-9c0b-5802-ac76-5d4a0f818b3b, ff3eaabd-1ab7-5fd1-99b6-9fb365b10330 |  | 1 |
| 5d02aa25-105a-4865-839f-bc6eb2f3e219 | CLAIM_DETAIL | The document subtype is Motor Third-Party Claim - Insured's Handwritten Statement. | 1.00 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | ba125025-d830-5791-9123-b177911fe7f5 |  | 0 |
| c4288799-7d3c-4be5-b50f-1a729e5147b1 | CLAIM_DETAIL | The document type is insured_statement. | 1.00 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | e1bf420d-a0bc-538c-8ce1-1d11cd226f2e |  | 1 |
| fc004856-8687-40c1-93c6-13b570bae640 | PERSONAL_INFO | Mahesh Jyear is associated with the document in an administrative capacity. | 0.85 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | cfb7bb4c-57aa-59a3-ae71-893a5d7ea384, 25f8e86f-af5d-51e8-922d-b933b929ee76 |  | 1 |
| 2b97ffd4-c4de-42a4-add1-669007d0afe1 | LOCATION | The country mentioned in the statement is India. | 0.95 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | 33baba70-e4a4-554c-a849-d9597748a36a |  | 1 |
| 707c1616-9e61-4db6-9655-1823600bb0c1 | CLAIM_DETAIL | The document contains a handwritten signature at the bottom. | 0.90 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | 33baba70-e4a4-554c-a849-d9597748a36a |  | 0 |
| 905fe62f-003a-4482-8592-91ead6c05e97 | INCIDENT | The statement contains a handwritten narrative in Gujarati describing accident or incident circumstances. | 0.70 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | 33baba70-e4a4-554c-a849-d9597748a36a, 47c9c8b5-c0ab-58f1-bdf1-b68e8189e774 |  | 0 |
| b74322fc-73dd-44fe-af18-f40f396594c4 | CLAIM_DETAIL | The document language is Gujarati. | 1.00 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | 47c9c8b5-c0ab-58f1-bdf1-b68e8189e774 |  | 0 |
| 29524d03-25f0-465f-95dc-0fa84c97f1d5 | PERSONAL_INFO | The contact phone number is +919227637160. | 0.95 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | 33baba70-e4a4-554c-a849-d9597748a36a, 84beac75-9e61-579e-882c-50bb1e5a6ac7 |  | 1 |
| 915047fc-f133-47e9-8bd5-7dd4e7d1beaf | CLAIM_DETAIL | The claim reference number is OC-24-2203-1801-00002660. | 1.00 | 222696526_Statement_of_Insured.pdf / 222696526_Statement_of_Insured / insured_statement | 25f8e86f-af5d-51e8-922d-b933b929ee76, 23d9b964-fb82-5dd1-a873-588913a5f6ea |  | 1 |
| 3b7ade32-fd60-4fc0-aeeb-c5a7bf7452e3 | CLAIM_DETAIL | The policy number is OG-24-2203-1801-00005412. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e400b380-1a48-5c23-bb3c-6cc0a1a727fc, 449481ae-120d-54ea-b358-8077108e10d3 |  | 1 |
| 61c8cdf9-ca09-4f15-8be6-384bfeab6fc6 | LOCATION | The driver address is B M COMPLEX, NANA VARACHHA, SURAT. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fda88858-e4cd-59ca-b9b8-93c90186aff5, c81afe29-c322-537c-8f29-2c42495ba4b4, fb54b9d1-a063-50fb-8e1d-e7040e6a8561 (+2 more) |  | 2 |
| ee0b7c21-585f-42be-af0d-9d176d19fda6 | PERSONAL_INFO | The driver contact number is +918306895545. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | ddf770a6-d76d-5b18-826d-46f8d25fd3cc, c81afe29-c322-537c-8f29-2c42495ba4b4 |  | 2 |
| fc86fadf-d134-4bd3-bb08-aa0152f885d9 | PERSONAL_INFO | The driver driving license number is GJ05/028137/06. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | a254c8b3-601d-5d72-8eaf-b627f5291607, c81afe29-c322-537c-8f29-2c42495ba4b4 |  | 2 |
| 596765c8-179f-4bb5-8a9c-01b890898aa9 | PERSONAL_INFO | The driver driving license is authorized for LMV N/T. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | c81afe29-c322-537c-8f29-2c42495ba4b4 |  | 1 |
| f20b263b-4334-4bc0-96f9-2a4c98972efe | DATE_TIME | The driver driving license validity is from 2006-04-12 to 2026-04-11. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | c81afe29-c322-537c-8f29-2c42495ba4b4 |  | 3 |
| c9c7f929-07fa-40ad-af10-d64e0bf4c5e2 | INCIDENT | The accident occurred on 2023-08-08 at approximately 21:00 at Nana Varachha in front of Moti Nagar, Surat. | 0.85 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e400b380-1a48-5c23-bb3c-6cc0a1a727fc, fda88858-e4cd-59ca-b9b8-93c90186aff5, 9ab05a69-002a-532f-8fb1-935fb1a9fa5e (+3 more) |  | 3 |
| 4b5d37f5-a48f-477f-a4e7-2651646ffe5d | INCIDENT | A motorcycle came from the wrong side during the accident. | 0.85 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 02c6de25-71fa-4637-a17a-c0d91e318db4 | INCIDENT | The driver pressed the accelerator instead of the brakes to avoid the motorcycle. | 0.85 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 82a8d15b-7f67-4b00-adc6-4bf61cf1196a | INCIDENT | The vehicle dashed into the divider. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| a24c699c-e237-4b83-ad53-379655c016f2 | INCIDENT | There were only two people in the vehicle at the time of the accident. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| a5b1717b-dc64-4890-9be3-2f65f0d5f3f6 | MEDICAL | No one was injured in the accident. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 8c4d7690-f878-44c1-9d23-5e272a730d59 | LEGAL | No police complaint was filed for the accident. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 9662287f-743d-4428-8681-96af45bc960e | INCIDENT | The vehicle was damaged on the front side. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 38c5f96c-a0c1-416b-94d1-2ad17a6e4331 | INCIDENT | The vehicle was towed to Navjivan Hyundai Garage. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fda88858-e4cd-59ca-b9b8-93c90186aff5, fb180e25-bc3a-5cac-a087-826c640a91da, 8d31b582-b293-5687-925a-9a0d9c86d743 |  | 2 |
| 808b5bc3-12a9-4234-b6a7-2d192901432e | LOCATION | The garage name is Navjivan Hyundai Garage. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fda88858-e4cd-59ca-b9b8-93c90186aff5, fb180e25-bc3a-5cac-a087-826c640a91da, 8d31b582-b293-5687-925a-9a0d9c86d743 |  | 1 |
| b11949ad-dd03-488f-bcca-664a054c2ab6 | LOCATION | The garage address is Nr. SMC south Zone office, DevChand Nagar, Udhana, BAMROLI, SURAT, GUJARAT 394210. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | 668d4e57-70a1-539a-b177-3ee719fa8d35, fda88858-e4cd-59ca-b9b8-93c90186aff5, f970411b-1af7-572f-a4d3-a81d19c6b1e6 |  | 2 |
| dd126df3-2578-4efb-b481-55f20e2ab4fe | LOCATION | The garage is a non-network garage. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fda88858-e4cd-59ca-b9b8-93c90186aff5 |  | 1 |
| 8d4bd7d9-2f7b-43f1-8557-9b7c9792498a | DATE_TIME | The job card date is 2023-08-09. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fda88858-e4cd-59ca-b9b8-93c90186aff5 |  | 1 |
| 11e35d3e-0b03-4896-aa37-5e55014fa4dd | LOCATION | The accident spot location is Nana Varachha, Surat with landmark Moti Nagar Society. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fda88858-e4cd-59ca-b9b8-93c90186aff5, 9ab05a69-002a-532f-8fb1-935fb1a9fa5e, fb54b9d1-a063-50fb-8e1d-e7040e6a8561 (+2 more) |  | 2 |
| 506e6d89-3b64-4a79-b77c-28bbeded48ec | INCIDENT | There was no eyewitness at the accident spot. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 47ecc22c-57f9-4f6b-9db1-032de6ca8abc | INCIDENT | There were no CCTV cameras at the accident spot. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 19d5d986-2f8e-47a6-bc58-2914189a2891 | INCIDENT | No photographs were taken at the accident spot. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 388ebfef-4b21-4b44-836a-615ab0f56fd4 | PERSONAL_INFO | The insured does not know how to drive. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 8e63701b-9534-4cd4-a59d-6ec13b9b8980 | RELATIONSHIP | The insured informed his friend Prakash Chaudhari to drive the vehicle when required. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 2 |
| 6073476d-a374-4a82-8068-f1749b14e357 | RELATIONSHIP | Prakashbhai Chaudhari works in the same lab as the insured. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | a0fee6dc-a6e9-59d9-a046-506ed2da8673, c81afe29-c322-537c-8f29-2c42495ba4b4 |  | 3 |
| 61b5db64-21d7-41c6-aa97-0560687fa96d | DATE_TIME | The report date is 2023-09-18 at 14:57:46. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e0a0e9bc-5da6-5426-bafd-cddc16de9526, bb53a42d-d311-566b-af16-1f87e95e5726 |  | 1 |
| 61473548-c0a8-4ec6-9e8c-92be08ca18bc | CLAIM_DETAIL | The intimation days to the company is 0. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 88f8e73d-8447-4c48-8982-adf269a31c5c | CLAIM_DETAIL | The referral days for investigation is 9. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 81ab4a8c-e845-4cf9-9552-7bb5fcdece9b | INCIDENT | During investigation, the insured initially stated the driver was Prakashbhai Chaudhari. | 0.85 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | a0fee6dc-a6e9-59d9-a046-506ed2da8673, c81afe29-c322-537c-8f29-2c42495ba4b4 |  | 2 |
| 9048b7dd-5a4c-4100-bfef-6443f3d7a3f0 | INCIDENT | Upon further investigation, the insured admitted he was actually driving the vehicle. | 0.85 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 5bddb55a-95ed-434b-8f7f-c87e3c6d94e9 | PERSONAL_INFO | The insured does not have a valid driving license (MDL). | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 6e93590b-c874-4871-ab87-c2b6d9c99c50 | INCIDENT | The insured provided his friend's driving license instead of his own. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 2 |
| 8f59fb25-165c-4063-8977-83e10d8b470a | VEHICLE_INFO | The vehicle purchase was verified at Bappa Sitaram Car Mela on 2023-08-03. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | 58546879-4ba3-5e22-99fb-6962eb489736, e400b380-1a48-5c23-bb3c-6cc0a1a727fc, fb180e25-bc3a-5cac-a087-826c640a91da |  | 3 |
| 9dcfac24-20db-48e7-886f-d38411dce022 | INCIDENT | The insured was photographed receiving the vehicle key at Bappa Sitaram Car Mela. | 0.85 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | 58546879-4ba3-5e22-99fb-6962eb489736, fb180e25-bc3a-5cac-a087-826c640a91da |  | 2 |
| 2258cc92-a3f3-4d01-ad4a-3c8c8f9929ab | INCIDENT | The investigation confirmed that the driver was changed in the case. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| ccca29be-02c0-4dea-8df5-6cd0e31b4f46 | INCIDENT | The insured was driving without a valid driving license. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 2e9c1844-e589-47bf-bd92-a3888efa67b0 | CLAIM_DETAIL | The insured has withdrawn the claim. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 18db3d48-eb2b-4fce-85b1-0cb194def2b5 | INCIDENT | A withdrawal statement and video recording were taken from the insured. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| da2cf96e-48f4-4365-9099-ddabb29bb7da | INCIDENT | Driver implant flag is marked as Yes in QC1. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 2e76680c-0ded-4b95-b997-9abe20c0ee1e | INCIDENT | Vehicle damage is on the driver side. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 7e6fe219-b2c2-4aea-8ccf-a766468dc1b6 | MEDICAL | No driver injury was provided. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 44c6f1ba-4c90-4ef3-9a79-a193ff9e6e34 | CLAIM_DETAIL | There is no delay in the intimation. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 0 |
| 8b2e3628-eb14-4103-bbae-b0318aceaab4 | VEHICLE_INFO | The vehicle was purchased on 2023-08-03 from Bappa Sitaram Car Mela. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | 58546879-4ba3-5e22-99fb-6962eb489736, e400b380-1a48-5c23-bb3c-6cc0a1a727fc, fb180e25-bc3a-5cac-a087-826c640a91da |  | 3 |
| 3e635182-432c-4daf-bae7-8f76864ff303 | VEHICLE_INFO | The vehicle make year is 2013. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fb180e25-bc3a-5cac-a087-826c640a91da |  | 1 |
| dda85dbc-4c7e-467a-9b63-48d09dcce4df | DATE_TIME | The vehicle registration date is 2013-10-17. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fb180e25-bc3a-5cac-a087-826c640a91da |  | 2 |
| d52a9d57-7c2a-4182-a1c9-caa15e108cfc | VEHICLE_INFO | The vehicle is hypothecated to Bajaj Finance. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | 1db58b3e-8c2f-5f4b-abcd-f030968a543c, fb180e25-bc3a-5cac-a087-826c640a91da |  | 2 |
| f20890a8-3229-411c-a965-e0354d8e4432 | VEHICLE_INFO | The vehicle chassis number is MALA351ALDM226944. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | 5069e4f6-4d24-5c6f-91ca-ada1df61d9d2, fb180e25-bc3a-5cac-a087-826c640a91da |  | 2 |
| 9f3db6dc-8eeb-4629-ab81-233469b4dce5 | VEHICLE_INFO | The vehicle engine number is G3HADM199. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | f699d483-d482-5432-b81c-ac8cb5803645, fb180e25-bc3a-5cac-a087-826c640a91da |  | 2 |
| 6f5d11c2-5e07-4601-9b57-675512ec1160 | VEHICLE_INFO | The vehicle model is EON. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| d42e1f0e-cb5b-4d0f-97e8-018320831afa | VEHICLE_INFO | The vehicle make is HYUNDAI. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fb180e25-bc3a-5cac-a087-826c640a91da |  | 1 |
| 74c8a7e5-f109-43dd-971a-aa6879417c70 | VEHICLE_INFO | The vehicle class is Private Car. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | fb180e25-bc3a-5cac-a087-826c640a91da |  | 1 |
| 525bd3ca-a5ab-46f9-9af0-c952dc9d083c | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | 21f09fb5-1872-5b63-adcb-19f9c6011a0e, fb180e25-bc3a-5cac-a087-826c640a91da |  | 1 |
| d6ee6290-f6d7-4c7c-85df-a6ab28fa718c | PERSONAL_INFO | The insured is living with his wife and 7-year-old daughter. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence |  |  | 1 |
| 63f42fcc-45cd-4c36-9f06-0d1e36f382ec | PERSONAL_INFO | The insured has been working at Radhi Lab for 3 years. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | cafaa179-c204-502c-969c-17e342965000 |  | 1 |
| 788dd1d3-c10c-494f-9766-4c17186a87bd | PERSONAL_INFO | The insured works as a technician at Radhi Lab. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | cafaa179-c204-502c-969c-17e342965000, f970411b-1af7-572f-a4d3-a81d19c6b1e6, 64baded4-5bad-5979-800f-61e69670f0fb |  | 2 |
| c597d7e3-a682-4cc3-81bc-5a14d4590270 | PERSONAL_INFO | The driver name is Prakashbhai Chaudhari. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | a0fee6dc-a6e9-59d9-a046-506ed2da8673, c81afe29-c322-537c-8f29-2c42495ba4b4 |  | 1 |
| e1580488-7645-4721-8ebf-5f0ebe913b4c | PERSONAL_INFO | The insured contact number is +919773228144. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | f970411b-1af7-572f-a4d3-a81d19c6b1e6, 26c97d80-c093-5fc3-ab92-dd9cc03d0ef5 |  | 2 |
| 4df8adef-fb2f-44bd-a0e6-fa74bbf01f4a | LOCATION | The insured postal address is 6 NANA VARACHHA HOUSING SOCIETY, NANA VARACHHA DHAL, NANA VARACHHA, KAMREJ ROAD, SURAT CITY, SURAT, GUJARAT 395006. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | d82d4e43-efcf-5bbf-8331-d0a9200450df, fda88858-e4cd-59ca-b9b8-93c90186aff5, f970411b-1af7-572f-a4d3-a81d19c6b1e6 |  | 2 |
| 87db079c-9039-44b6-990b-6dd5f477824d | PERSONAL_INFO | The insured occupation is Pvt. Service. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | f970411b-1af7-572f-a4d3-a81d19c6b1e6 |  | 1 |
| d77b0ed3-c547-4b41-a3ce-77163992c80f | PERSONAL_INFO | The insured PAN number is BOTPV1128N. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | d30dd126-4aab-5cf4-8656-fa303d616671, f970411b-1af7-572f-a4d3-a81d19c6b1e6 |  | 2 |
| bf45f508-67af-40b0-a950-e7e02f1d0071 | PERSONAL_INFO | The insured date of birth is 1988-09-13. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | f970411b-1af7-572f-a4d3-a81d19c6b1e6 |  | 2 |
| 79f8e8df-d7fe-4332-8e20-b7e511aef2bb | PERSONAL_INFO | The insured name is Maheshkumar Indrasing Vasava. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | f970411b-1af7-572f-a4d3-a81d19c6b1e6, 64baded4-5bad-5979-800f-61e69670f0fb |  | 1 |
| 10394f93-756c-4122-81b4-19c2222f8488 | DATE_TIME | The claim was referred to investigation on 2023-08-18. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e400b380-1a48-5c23-bb3c-6cc0a1a727fc |  | 1 |
| b98507b6-36c7-4083-8a0c-14c3264e5bdd | DATE_TIME | The date of claim registration is 2023-08-10. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e400b380-1a48-5c23-bb3c-6cc0a1a727fc |  | 1 |
| 96e307da-3b81-4615-bd6e-fb067b00ae7d | DATE_TIME | The date of loss is 2023-08-08. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e400b380-1a48-5c23-bb3c-6cc0a1a727fc, 67038433-1c1b-5a9b-91aa-4baa13d1804c |  | 1 |
| 887a4e29-8e80-4f9d-9f9e-59a8fceca85e | CLAIM_DETAIL | The product name is Private Car - Package Policy. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e400b380-1a48-5c23-bb3c-6cc0a1a727fc, fb180e25-bc3a-5cac-a087-826c640a91da |  | 0 |
| e5968010-468b-4cee-b024-2cb1e1604137 | CLAIM_DETAIL | The policy period is from 2023-08-03 to 2024-08-02. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e400b380-1a48-5c23-bb3c-6cc0a1a727fc, fb180e25-bc3a-5cac-a087-826c640a91da |  | 2 |
| 69e05c52-a9fb-497f-bf02-7f9c78c8bdf6 | CLAIM_DETAIL | The claim number is OC-24-2203-1801-00002660. | 0.95 | 223214762_Investigation_Report.pdf / 223214762_Investigation_Report / correspondence | e400b380-1a48-5c23-bb3c-6cc0a1a727fc, f1fc68c5-b192-5b09-bc79-f09fa212155d |  | 1 |
| 88b5f5ad-2ad8-4606-8bef-6ce6c9e5d9d3 | INCIDENT | There was no eyewitness or CCTV cameras at the accident spot. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 0 |
| b3ca1269-d00b-4bd6-864a-336c4e50c7a8 | MEDICAL | No driver injury was provided. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 0 |
| 51e31ae6-3939-47ec-93c6-95900b28ae4d | INCIDENT | The vehicle damage is on the driver side. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 1 |
| cb75bb4a-9bd4-424b-ad59-ba4ce6c66d92 | INCIDENT | A driver implant flag has been marked in QC1. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 0 |
| 3c465fed-257a-4e23-aac2-99c867fcb0df | CLAIM_DETAIL | The insured has withdrawn the claim. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 1 |
| 4f2356c8-3cca-4483-9d48-e946b12279f1 | INCIDENT | The vehicle was confirmed to have been purchased on 2023-08-03 from Bappa Sitaram Car Mela. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357, 9a076daf-aac2-5c04-b199-0182d8abcd1f, 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 3 |
| b5224971-1077-4c8a-91ec-1cb94fedecb4 | INCIDENT | The insured used his friend's driving license instead of his own. | 0.80 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 2 |
| 5db50a99-d78c-4d67-9de2-853e9702dc44 | INCIDENT | Upon further investigation, the insured admitted that he was actually driving the vehicle and does not have a valid driving license. | 0.80 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 1 |
| 743e1727-6efd-4e23-aa11-84be85cf579b | INCIDENT | During investigation, the insured initially stated that his friend Prakashbhai Chaudhari was driving the vehicle. | 0.80 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | f50918c9-dcc5-5ca8-ba2c-5588e09378c7, 9936a4c0-c8c8-5b3e-8ae9-a36fae048379, 008a86f5-43f5-57cc-9476-bbcba71abe80 |  | 2 |
| 73f8aed8-09c0-4317-b200-a54364a617d5 | DATE_TIME | The investigation report date is 2023-09-18 at 14:57:46. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 46a65c5a-ae12-5e76-bf42-6ee921e951e6 |  | 1 |
| 375cf7ac-d85e-4667-ade9-29c16fc176d6 | INCIDENT | No eyewitness is available for the incident. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 0 |
| 9089a512-0d2e-48e9-864d-d14af32163c3 | LOCATION | The accident spot is located at Nana Varachha, Surat with landmark Moti Nagar Society. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | bede577e-d0fa-571d-95f5-bccc822ba538, 0d7f0f9e-40b5-5c33-aca2-5aa071268458, 9139824f-45d4-5ade-a794-76ef921af652 (+4 more) |  | 2 |
| a93cb145-628e-40c0-bdc9-4569fb9c4127 | INCIDENT | The garage is a non-network garage. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 1 |
| dfa61523-9cc2-4a0f-b73f-48a07cbaff25 | LOCATION | The garage is located in BAMROLI, SURAT district, GUJARAT state, pin code 394210. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 0d7f0f9e-40b5-5c33-aca2-5aa071268458, caf77add-42b8-51a9-a3ec-be40aed584cc, 18708e92-9615-578b-a6d4-61805379d0b0 (+1 more) |  | 4 |
| 7beb767d-06d1-4aca-930a-d540467bfc64 | LOCATION | The garage is Navjivan Hyundai Garage located at Nr. SMC south Zone office, DevChand Nagar, Udhana, Surat. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 0d7f0f9e-40b5-5c33-aca2-5aa071268458, a20c7122-359f-5fa8-b03a-cafbe1f9dc50, 9c834d5b-2a79-52ee-8ecc-30cef3c35357 (+2 more) |  | 2 |
| 66038007-bcb7-4ee3-afea-a8f1a500a3fd | DATE_TIME | The workshop gate entry job card date is 2023-08-09. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 18708e92-9615-578b-a6d4-61805379d0b0 |  | 1 |
| a989511f-98c5-48f0-b483-097af669ba8e | INCIDENT | The vehicle was towed to Navjivan Hyundai Garage workshop. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | a20c7122-359f-5fa8-b03a-cafbe1f9dc50, 18708e92-9615-578b-a6d4-61805379d0b0, 9c834d5b-2a79-52ee-8ecc-30cef3c35357 |  | 2 |
| 2114d2ed-8198-4ca1-a3e7-bd33084be873 | LEGAL | No police complaint was filed for the incident. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 0 |
| 6fd48a0b-0d3a-41dd-b039-5f55f4151662 | INCIDENT | No one was injured in the incident. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | bede577e-d0fa-571d-95f5-bccc822ba538 |  | 0 |
| 02827a0c-92e1-445e-86bb-90d0eefe7003 | INCIDENT | The vehicle dashed into the divider during the incident. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence |  |  | 1 |
| de0affa1-4fdd-4406-8fc1-27d9a1d9c13e | INCIDENT | A motorcycle came from the wrong side during the incident. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | bede577e-d0fa-571d-95f5-bccc822ba538 |  | 0 |
| 7fb98498-4948-4de4-af32-aa959891bb19 | INCIDENT | The incident occurred on 2023-08-08 at approximately 21:00 at Nana Varachha, Surat near Moti Nagar Society. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | bede577e-d0fa-571d-95f5-bccc822ba538, 0d7f0f9e-40b5-5c33-aca2-5aa071268458, 9139824f-45d4-5ade-a794-76ef921af652 (+5 more) |  | 3 |
| 4546ce8d-4e04-4daf-b0b8-930765c1091b | DATE_TIME | The driver license validity is from 2006-04-12 to 2026-04-11. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9936a4c0-c8c8-5b3e-8ae9-a36fae048379 |  | 3 |
| 4cc11def-6175-4eb2-a086-5d3f44412e74 | PERSONAL_INFO | The driver is authorized to drive LMV N/T. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9936a4c0-c8c8-5b3e-8ae9-a36fae048379 |  | 1 |
| 521cc554-8220-404e-bada-ad372e9c858a | PERSONAL_INFO | The driver driving license number is GJ05/028137/06. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9936a4c0-c8c8-5b3e-8ae9-a36fae048379, 0971b3e9-3bd5-5ef6-b5ef-9ee98e34fc7f |  | 2 |
| 0e52061d-38e7-462d-a794-561b11d7f37d | PERSONAL_INFO | The driver contact number is +918306895545. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9936a4c0-c8c8-5b3e-8ae9-a36fae048379, c6827afd-1a86-5cf9-8fe0-96634f2b7619 |  | 2 |
| 63e5b3b0-a3a7-483a-8eee-7df14486fb6b | PERSONAL_INFO | The driver address is B M COMPLEX, NANA VARACHHA, SURAT. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 0d7f0f9e-40b5-5c33-aca2-5aa071268458, 26ea46fc-b9b3-55a8-8dbe-036a1da278a3, 9936a4c0-c8c8-5b3e-8ae9-a36fae048379 (+3 more) |  | 2 |
| b21fd0c2-b57e-476a-93f7-e89d5de21d1a | PERSONAL_INFO | The driver name is Prakashbhai Chaudhari. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9936a4c0-c8c8-5b3e-8ae9-a36fae048379, 008a86f5-43f5-57cc-9476-bbcba71abe80 |  | 1 |
| 8b8aa8ae-bdc8-4645-a81a-a89e6936bd40 | DATE_TIME | The vehicle was purchased on 2023-08-03 at 14:30 from Bappa Sitaram Car Mela. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357, 9a076daf-aac2-5c04-b199-0182d8abcd1f, 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 3 |
| 4bbb9728-7e28-45fd-9593-80b07e72495c | VEHICLE_INFO | The vehicle make year is 2013. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357 |  | 1 |
| 184c5e80-c881-488e-9210-824d0bbcf99e | DATE_TIME | The vehicle registration date is 2013-10-17. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357 |  | 2 |
| d0d32710-2ad5-4b9d-8441-9e785aff9ff8 | VEHICLE_INFO | The vehicle is hypothecated to Bajaj Finance. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 0c7cc7b9-9a84-56bb-b6ac-eeff20431064, 9c834d5b-2a79-52ee-8ecc-30cef3c35357 |  | 2 |
| 01a042a1-9a67-46fa-9b08-ed55b215b4b0 | VEHICLE_INFO | The vehicle chassis number is MALA351ALDM226944. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357, 735b98bb-9212-5c81-9e4a-e24a520c3364 |  | 2 |
| 622ae3c5-1339-45d8-a41c-761b99e6e2d9 | VEHICLE_INFO | The vehicle engine number is G3HADM199. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | e1881bbc-912e-5c3d-b62b-d2c55aa70df2, 9c834d5b-2a79-52ee-8ecc-30cef3c35357 |  | 2 |
| 60a652f6-11d8-4b3c-a2e1-86c29b682ff6 | VEHICLE_INFO | The vehicle make is HYUNDAI and model is EON. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357 |  | 1 |
| 66c3a406-1b57-46d1-a9c4-f2717451ab42 | VEHICLE_INFO | The vehicle class is Private Car. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357 |  | 1 |
| 6b2d789a-6ec3-42fe-9b63-bccbd634b0e5 | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357, 0252b49b-2c3c-5625-9c7a-a6c4e6871530 |  | 1 |
| 53041d18-9c20-4e46-9174-61452bb146a6 | PERSONAL_INFO | The insured is living with his wife and 7-year-old daughter. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | f50918c9-dcc5-5ca8-ba2c-5588e09378c7 |  | 1 |
| 4f618b65-cf23-4168-bf3b-a1113a66ffae | PERSONAL_INFO | The insured works as a technician at Radhi Lab and has been working there for 3 years. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 481b163b-7728-5bcb-9d85-df2e1c4db92d, f50918c9-dcc5-5ca8-ba2c-5588e09378c7 |  | 2 |
| 408a21c6-f8d5-407f-85b1-b1b3c10e1b7d | PERSONAL_INFO | The insured contact number is +919773228144. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | e8c083aa-9d5e-5e29-be20-6939d4a80bab, f50918c9-dcc5-5ca8-ba2c-5588e09378c7 |  | 2 |
| bd8ebbd8-a1e3-40d6-8cb9-72d61ef6b176 | LOCATION | The insured district is SURAT, state is GUJARAT, and pin code is 395006. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 0d7f0f9e-40b5-5c33-aca2-5aa071268458, caf77add-42b8-51a9-a3ec-be40aed584cc, 18708e92-9615-578b-a6d4-61805379d0b0 (+1 more) |  | 3 |
| a4aaf865-2e36-4644-91a5-8d74db6b6061 | INCIDENT | The vehicle was damaged on the front side. | 0.85 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | bede577e-d0fa-571d-95f5-bccc822ba538 |  | 1 |
| 940a061c-86d0-4aef-bdc0-69573aeba539 | PERSONAL_INFO | The insured postal address is 6 NANA VARACHHA HOUSING SOCIETY, NANA VARACHHA DHAL, PO and Village NANA VARACHHA, KAMREJ ROAD, SURAT CITY. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 0d7f0f9e-40b5-5c33-aca2-5aa071268458, 18708e92-9615-578b-a6d4-61805379d0b0, f50918c9-dcc5-5ca8-ba2c-5588e09378c7 |  | 2 |
| 32e97d2a-2020-46b4-a07f-96d664d90e35 | PERSONAL_INFO | The insured occupation is Pvt. Service. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | f50918c9-dcc5-5ca8-ba2c-5588e09378c7 |  | 1 |
| ee773d7d-a483-4b01-9cbb-5773af2ded6d | PERSONAL_INFO | The insured PAN number is BOTPV1128N. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | f50918c9-dcc5-5ca8-ba2c-5588e09378c7, f21828e7-2f93-57c3-a84e-4702ee0ddba8 |  | 2 |
| 91fa1d85-1810-453e-9195-d323e2d31773 | PERSONAL_INFO | The insured date of birth is 1988-09-13. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | f50918c9-dcc5-5ca8-ba2c-5588e09378c7 |  | 2 |
| fef45fde-86c1-40d9-97a0-dd1565e1a3e2 | PERSONAL_INFO | The insured name is Maheshkumar Indrasing Vasava. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | f50918c9-dcc5-5ca8-ba2c-5588e09378c7, efc7d9c4-675e-5cdf-912c-2977c0a08394 |  | 1 |
| f7d658d7-e8c2-4779-b316-226ff48a1d2a | DATE_TIME | The claim was referred to investigation on 2023-08-18. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 1 |
| f020acbd-7b6f-4198-9894-41237c1acadf | DATE_TIME | The date of claim registration is 2023-08-10. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 1 |
| 97ab6a6f-35e7-4d13-a3ba-770dc575d3c6 | DATE_TIME | The date of loss is 2023-08-08. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | bede577e-d0fa-571d-95f5-bccc822ba538, 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 1 |
| 3e7571d0-3287-4617-ba93-7cc27de7aa08 | CLAIM_DETAIL | The product name is Private Car - Package Policy. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357, 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 0 |
| 877e9103-f081-4e5c-bd38-93280148fe7f | CLAIM_DETAIL | The policy period is from 2023-08-03 to 2024-08-02. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 9c834d5b-2a79-52ee-8ecc-30cef3c35357, 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 2 |
| 3cf71f67-a4c2-4a69-b805-5b41c7373c0c | CLAIM_DETAIL | The policy number is OG-24-2203-1801-00005412. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | 2e285ee7-8ee2-547c-9099-49a11b8ce00c, 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 1 |
| f40cb288-0055-4b43-be6c-1e944a2933fb | CLAIM_DETAIL | The claim number is OC-24-2203-1801-00002660. | 0.95 | 223215102_Investigation_Report.pdf / 223215102_Investigation_Report / correspondence | d87f94a5-42d6-5c50-bf9b-88ab681c99a2, 64e45581-57d4-5b7f-afaa-0e5036ff8b15 |  | 1 |
| eb54d727-2f84-4148-85fa-66777f86376c | FINANCIAL | The professional fee for spot survey is INR 1,500.00. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | e39c9348-b4aa-5267-844b-4807d1eb1705, 64588f90-6fcd-5cb7-9761-d53d5a260717, f9ba9850-3254-5409-8919-0fc8b1e6d627 |  | 1 |
| 8ac4f39d-4ebe-447f-881e-fdc5619705e9 | FINANCIAL | The professional fee for final survey is INR 1,500.00. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 64588f90-6fcd-5cb7-9761-d53d5a260717, f9ba9850-3254-5409-8919-0fc8b1e6d627 |  | 1 |
| d1ce50fc-5384-444c-8bef-27076a8e0c75 | FINANCIAL | The conveyance charge is INR 750.00. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 406faafc-4b23-5f2e-aca6-66dd04a1ffd0, 77c1745f-1197-54d3-b5d7-c24cd214e78b |  | 1 |
| f93d7ffc-d1b2-463f-bd46-ccd9aa4135fe | FINANCIAL | The total professional fees before tax is INR 2,250.00. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 99073406-2c63-5381-8963-c7e1b9a71d48, f9ba9850-3254-5409-8919-0fc8b1e6d627 |  | 1 |
| 25f887bb-f528-4d0c-8d91-4a532c0fd30d | FINANCIAL | The CGST at 9% is INR 202.50. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f9ba9850-3254-5409-8919-0fc8b1e6d627, 710e64e8-43e3-5933-85c9-7ef85176940f, 55762fd2-cb65-5db7-a889-1a99b5382989 |  | 1 |
| 2b61896d-fbdf-4689-a728-09e0d1bffaff | FINANCIAL | The SGST at 9% is INR 202.50. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f9ba9850-3254-5409-8919-0fc8b1e6d627, 710e64e8-43e3-5933-85c9-7ef85176940f, 55762fd2-cb65-5db7-a889-1a99b5382989 |  | 1 |
| bba72994-23f7-4ecb-b00d-737f948aa85e | FINANCIAL | The total tax is INR 405.00. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | da9baa82-bab8-5630-af54-fc4f29f6474b |  | 1 |
| 0fa48cdc-35c5-414c-aad8-0704ea092e9a | FINANCIAL | The total amount with tax is INR 2,655.00. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 5474909b-3958-5c27-a55a-09ceac120b8a, f9ba9850-3254-5409-8919-0fc8b1e6d627 |  | 1 |
| 2fdc1dcb-e44c-4e5d-984e-b9e73cda603e | PERSONAL_INFO | The surveyor's GSTIN is 24AJAPD2623K12N. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f4ba3f8e-8404-5f75-82d1-cbab53cde06f, b4e48232-8a37-503b-9543-22a263acbfb0 |  | 1 |
| d0d0d841-5aaa-4bf1-94af-122e26fbc3a6 | PERSONAL_INFO | The surveyor's PAN is AJAPD3623K. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f4ba3f8e-8404-5f75-82d1-cbab53cde06f, 2370200f-39d0-5d7f-86ac-dc77bcebf2db |  | 1 |
| 2c003ea8-754e-4596-9e15-7d8109066b12 | PERSONAL_INFO | The surveyor is Vivekkumar M. Desai. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f4ba3f8e-8404-5f75-82d1-cbab53cde06f, 40ef1e72-2fb3-586b-8dfa-a2438abf8ad0 |  | 1 |
| f9dbbd12-9850-43e6-8f32-22ea98a081ce | PERSONAL_INFO | The surveyor's license number is S.I.A. 73760. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 5898742a-64a1-5165-9a80-6e96a2800ddd, f4ba3f8e-8404-5f75-82d1-cbab53cde06f, 29dc3d15-5ba8-5260-b1f8-808645702e81 |  | 1 |
| a87848fc-f678-4980-b44d-df5414c1f945 | DATE_TIME | The surveyor's license is valid until 2024-10-03. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f4ba3f8e-8404-5f75-82d1-cbab53cde06f, 29dc3d15-5ba8-5260-b1f8-808645702e81 |  | 1 |
| f13aa7f7-446d-47bf-bdc1-9338bc4a372d | PERSONAL_INFO | The surveyor's licensiate membership number is L/W/06452. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f4ba3f8e-8404-5f75-82d1-cbab53cde06f, 29dc3d15-5ba8-5260-b1f8-808645702e81 |  | 1 |
| ca347980-9455-4d3e-8107-ee16948d9fb0 | LOCATION | The surveyor's address is 29, Anand Nagar Society, Morabagad, Rander Road, Surat - 395005. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 49eedaf9-d77a-5f2f-a5d4-70674e36075f, f4ba3f8e-8404-5f75-82d1-cbab53cde06f |  | 1 |
| 40b3d9c4-1061-46ff-9c3e-61be0afe3ae0 | PERSONAL_INFO | The surveyor's contact phone number is +919879666447. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f4ba3f8e-8404-5f75-82d1-cbab53cde06f |  | 1 |
| 308ed85a-9a3e-47ef-97cc-83644f93a01c | PERSONAL_INFO | The surveyor's email address is desaivk29@gmail.com. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | f4ba3f8e-8404-5f75-82d1-cbab53cde06f |  | 1 |
| 9a386f04-27ec-445f-a39b-6af95f6cdc93 | CLAIM_DETAIL | The bill number is 6331. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 9ea70aee-8444-5146-a443-1ce5465c2c64 |  | 1 |
| f7830aef-0ab7-481b-9ae4-621914a76ed5 | CLAIM_DETAIL | The reference number for the bill is 6331-28-2023-34. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 9ea70aee-8444-5146-a443-1ce5465c2c64, 87863a07-7d79-584e-977c-374aa5c271f6 |  | 1 |
| d914bd8f-d7bb-4071-8c48-acf7d2b0a8d6 | DATE_TIME | The bill date is 2023-09-18. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 0f57da99-3ba5-58a3-b632-1ec83b1d04fa |  | 1 |
| 2a5d53bf-1d92-4529-8bfa-e8c9803f105e | CLAIM_DETAIL | The insurer is Bajaj Allianz General Insurance Co. Ltd. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 2f26a52e-f566-5bb1-b3bb-0bd9c636cc9d, b646fde7-665f-5b76-99d7-c2ec70be4183, 7a37eb29-a0ce-5300-9a03-4562449f4ac4 |  | 1 |
| 2de34a97-1d79-4205-9b52-0dfac6bc2838 | LOCATION | The insurer's regional office address is 4th Floor, Atlantis Heritage, Opp-Deepali Petrol Pump, Sarabhai Road, Vadodara - 390007. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 704e3cc1-4ab9-5173-aa4b-79416b1cd2ce, 7a37eb29-a0ce-5300-9a03-4562449f4ac4 |  | 1 |
| 87eb6df9-f5c2-43ab-a9da-3cadb7340249 | CLAIM_DETAIL | The insurer's GSTIN is 24AABCB5730G1Z3. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 678d4869-29aa-52da-b276-9439a9ac5d6a, 7a37eb29-a0ce-5300-9a03-4562449f4ac4 |  | 1 |
| 8108c7ae-1723-4618-b256-7558cf276bf6 | CLAIM_DETAIL | The policy number is OG-24-2203-1801-06005412. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | b646fde7-665f-5b76-99d7-c2ec70be4183, 156cf79d-43e2-5ba8-9dcd-f2a711c1731a |  | 1 |
| 9431e8bc-86b6-43cb-8cd2-aff0ababf72d | CLAIM_DETAIL | The claim number is OC-24-2203-1801-00002600. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | b646fde7-665f-5b76-99d7-c2ec70be4183, 25d236b9-bd17-5f7b-82af-1b5d293af92f |  | 1 |
| c46f93de-0b4e-43bc-adb8-a6c52e81ba7a | CLAIM_DETAIL | The report number is VD/BAGIC/08/2023/6331. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 9ea70aee-8444-5146-a443-1ce5465c2c64, 004def89-2c8d-5dfd-b915-4b793616a6d4 |  | 1 |
| ddf819d0-54e0-4480-9fac-5a730517914e | PERSONAL_INFO | The insured is Maheshkumar Vasava. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | b646fde7-665f-5b76-99d7-c2ec70be4183, 92eaf22c-2682-51d8-a9b6-bdf219e1cc6f |  | 1 |
| 4711939f-43d2-4502-b219-e534a4fc163a | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 54f4f302-d337-5cad-a3db-0b80b1e8ade2, 8bad36a0-9cab-5905-a063-f67250b52498 |  | 1 |
| ad3ba200-5a2e-41d9-a4ed-142f39bb181f | VEHICLE_INFO | The vehicle make is H Eon. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 54f4f302-d337-5cad-a3db-0b80b1e8ade2, 29dc3d15-5ba8-5260-b1f8-808645702e81 |  | 1 |
| 9390c76a-577b-45e9-aa48-fe83fadd2d13 | FINANCIAL | The estimated loss is INR 96,000. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | de074bf4-bb78-5fcb-833d-c200721b81a1 |  | 1 |
| 6a0d81ff-1826-45ac-a35e-72628d8b3ff0 | DATE_TIME | The date of loss is 2023-08-06. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 004def89-2c8d-5dfd-b915-4b793616a6d4, f5a7455e-43c6-563e-bb94-da5639973546 |  | 1 |
| d8071691-5986-46bc-9269-1833087ddaf7 | DATE_TIME | The date of survey is 2023-08-11. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 004def89-2c8d-5dfd-b915-4b793616a6d4, 0945dca5-8fe0-5f8b-bb0d-0c90cd159e29 |  | 1 |
| ea247ff7-e34d-4c55-b193-8499b81e9f5c | LOCATION | The place of supply is Gujarat. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 004def89-2c8d-5dfd-b915-4b793616a6d4 |  | 1 |
| 0d9dac78-5566-4278-b191-5f354114d147 | LOCATION | The state of supply is Gujarat. | 0.95 | 223233211_Supplier_Bill.pdf / 223233211_Supplier_Bill / repair_estimate | 004def89-2c8d-5dfd-b915-4b793616a6d4 |  | 1 |
| a25e85fc-2b73-4e3b-8444-b60de7322c4c | FINANCIAL | The front side member assembly (RH) has a retail price of INR 2945, depreciation of INR 1178, and net assessed amount of INR 1767. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| d830b019-6839-473b-8db5-a077d74ac974 | FINANCIAL | The sealant kit has a retail price of INR 1024, depreciation of INR 512, and net assessed amount of INR 512. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| f138cc31-f3be-48d6-bbff-3686b174a079 | FINANCIAL | The cooling fan has a retail price of INR 588.01, depreciation of INR 294.01, and net assessed amount of INR 294. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 15ca73ad-496a-4cc2-b9b6-03f46109008b | FINANCIAL | The radiator assembly has a retail price of INR 2602.07, depreciation of INR 1301.04, and net assessed amount of INR 1301.03. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 87b9b495-6bd4-413f-8351-5094f13964b4 | FINANCIAL | The radiator shroud has a retail price of INR 346.79, depreciation of INR 173.4, and net assessed amount of INR 173.39. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 3700bb77-3989-48b5-9aed-40dc414f39f3 | FINANCIAL | The radiator cooling motor fan has a retail price of INR 3060.64, depreciation of INR 1530.32, and net assessed amount of INR 1530.32. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| d1e9b07e-7631-4c94-9bf6-c416f5b50900 | FINANCIAL | The right side cover panel has a retail price of INR 127.08, depreciation of INR 63.54, and net assessed amount of INR 63.54. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| f20300ac-1de0-4c9a-935b-e370ad812c75 | FINANCIAL | The front bumper cover has a retail price of INR 1604.99, depreciation of INR 802.5, and net assessed amount of INR 802.49. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 0e676789-4b57-4f8b-b53e-5e0b7907e4b5 | FINANCIAL | The front bumper grille has a retail price of INR 460.99, depreciation of INR 230.5, and net assessed amount of INR 230.49. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 148228ff-c0f0-409a-83d3-09f595b9ec02 | FINANCIAL | The total retail price for metal parts is INR 32537.41 with total depreciation of INR 13014.9 and total net assessed amount of INR 19622.45. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 924e26df-3569-49ec-b463-7153e55ec410 | FINANCIAL | The windshield glass part has a retail price of INR 4939.3 and net assessed amount of INR 4939.3. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 2 |
| 17d3e19f-45ef-462f-92af-2a535b20a7ac | DATE_TIME | The parts report was printed on 2023-09-18. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| e6143013-0dee-44e1-b2e6-ddd0b79f49f9 | DATE_TIME | The survey report date is 2023-08-12. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| b405acbd-149f-4555-aba8-84d4a3efe650 | LOCATION | The customer address is 6 NANA VARACHHA HOUSING SOCIETY, NANA VARACHHA DHAL NANA VARACHHA, KAM-REJ ROAD, SURAT CITY, SURAT. | 0.80 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 62ca588a-a885-4b28-a32f-66236f073728 | PERSONAL_INFO | The customer mobile number is +919773228144. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 4b880056-b7d1-46ae-aef2-d0129aabb886 | PERSONAL_INFO | The customer telephone number is +919773228144. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 8a55ee6b-9455-4d74-a59a-4e625da06af0 | PERSONAL_INFO | The customer name is MAHESHKUMAR VASAVA. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| cc059153-a4b6-49b8-8c0e-8c839ffc3087 | DATE_TIME | The policy expiry date is 2024-08-02. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| e15f9aed-2450-43a4-bf85-1596aef90f70 | DATE_TIME | The policy inception date is 2023-08-03. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| c214ab9a-03fc-4ff0-93c2-8fd71df617d3 | CLAIM_DETAIL | The claim ID is 31871257. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 175f50b3-e731-413b-abb8-c4bcae86a601 | CLAIM_DETAIL | The policy number is OG-24-2203-1801-00006412. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| f0fe163e-731c-4b2d-b4a7-ce7ea75825f6 | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 1ae30209-5e07-41e5-8643-bca0c6eda365 | CLAIM_DETAIL | The claim number is OC-24-2203-1801-00002660. | 0.95 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 6a502752-3aa8-4f37-959b-963cf22c2b54 | FINANCIAL | The front lower arm (LH) has a retail price of INR 730.41, depreciation of INR 292.16, and net assessed amount of INR 438.25. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 15abe997-3d14-4697-ac05-2b27baf0cff2 | FINANCIAL | The drive shaft assembly (LH) has a retail price of INR 6099.23, depreciation of INR 2439.69, and net assessed amount of INR 3659.54. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 100c0ef9-b6f9-4354-b3dc-6fb84c11f411 | FINANCIAL | The front lower arm (RH) has a retail price of INR 730.41, depreciation of INR 292.16, and net assessed amount of INR 438.25. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| cb12c40b-4c77-429c-9872-9ab621c23059 | FINANCIAL | The strut assembly has a retail price of INR 1208.37, depreciation of INR 483.35, and net assessed amount of INR 725.02. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| ecfe5dae-9639-4ed8-b294-8bc37e3fb6ea | FINANCIAL | The tie rod end assembly (LH) has a retail price of INR 608, depreciation of INR 243.2, and net assessed amount of INR 364.8. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 4f0b1e9b-13b6-4750-9b61-ef64c7e5d8c2 | FINANCIAL | The tie rod end assembly (RH) has a retail price of INR 608, depreciation of INR 243.2, and net assessed amount of INR 364.8. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| a05b6853-99ba-4220-8ca8-8057a7be79b2 | FINANCIAL | The inner ball joint assembly has a retail price of INR 879, depreciation of INR 351.6, and net assessed amount of INR 527.4. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 045a9379-8c46-4671-b277-f27cbe02257e | FINANCIAL | The front end module carrier assembly has a retail price of INR 5027, depreciation of INR 2010.8, and net assessed amount of INR 3016.2. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 9f16565f-8f4e-402f-a254-a558bba304c2 | FINANCIAL | The front side member assembly (LH) has a retail price of INR 3035.99, depreciation of INR 1214.4, and net assessed amount of INR 1821.59. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| f4bcab32-d5ff-4223-b209-12eb169a8b1a | FINANCIAL | The compressor assembly has a retail price of INR 10666, depreciation of INR 4266.4, and net assessed amount of INR 6399.6. | 0.92 | 223233267_Signed_Licensed_Surveyor_Report.pdf / 223233267_Signed_Licensed_Surveyor_Report / accident_report |  |  | 3 |
| 302087e0-b9e3-4ea6-9bc9-7652f32455e0 | VEHICLE_INFO | The vehicle chassis number is MALA351ALDM226944. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | d61540b4-7a02-5a19-85f3-c3522e570010, 1fb89263-3581-5618-b532-a54f9847e76d |  | 1 |
| a540fa03-9d13-4980-9226-1f097f11c4c4 | VEHICLE_INFO | The RTO endorsement for the vehicle is LMVNT. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 9edf3536-1633-5cc1-88b2-7cc328b01bee, 1fb89263-3581-5618-b532-a54f9847e76d, 59ff3ac1-d8ff-5194-a3ef-c7c78fef9a07 |  | 1 |
| d5f52a29-b76d-4c73-a311-886405ed5e9a | PERSONAL_INFO | The driving license endorsement is LMVNT. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 9edf3536-1633-5cc1-88b2-7cc328b01bee, 1fb89263-3581-5618-b532-a54f9847e76d |  | 1 |
| 62fea615-5ead-4b75-983e-c6612ea7ab5c | INCIDENT | The vehicle was not parked at the time of the incident. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 59ff3ac1-d8ff-5194-a3ef-c7c78fef9a07 |  | 1 |
| 331bf64e-002e-4f33-8bdd-427ccda23c74 | CLAIM_DETAIL | The parts report claim ID is 31871257. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 8e00dc56-7a54-597b-a2d1-3c685b0418fb, e3d55aeb-f74b-57e4-af4c-5b37dc4e8b98 |  | 1 |
| 916bfc57-a421-48e0-853e-f54d0e40dc24 | DATE_TIME | The report was printed on 2023-09-18 at 04:51:59. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 8cf758f8-59e7-4acf-aeae-f92f868b5c50 | PERSONAL_INFO | The surveyor is U.M.Desai. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | cd318f6a-29bb-5f64-bd6b-ae41332ab0e5 |  | 1 |
| 3637db6e-4e07-4b28-823f-a5a45144a4b7 | FINANCIAL | The net assessed amount (parts plus labour) is INR 77942. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | b5b0694a-fe11-5375-a7e3-9ea1c95c80f3 |  | 1 |
| e0d9d549-a4a8-4a64-b0bb-17cf726856d4 | FINANCIAL | The depreciation amount is INR 21462. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | acc916f4-6a09-5049-a8c6-91f00f016ca7 |  | 1 |
| 51c8b2f7-afb1-4ebf-91a0-bd43608c8c4b | FINANCIAL | The compulsory excess is INR 1000. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 30f2bf59-e26e-533c-91b6-24f476b6a4e0 |  | 1 |
| d8e588e3-e00e-40db-bc8b-370c97cb5d83 | FINANCIAL | The total assessed amount for labour is INR 49573. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 1d747cbf-145a-582e-8a9b-fd24e3e37415 |  | 1 |
| bbd42c13-d3b7-4cb8-a95e-36c399616981 | FINANCIAL | The total assessed amount for parts is INR 29369. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 5adc1af0-8659-5a24-9158-9eced5059d6d |  | 1 |
| 4e8935c8-3d60-4885-bc10-1e6869ae8861 | INCIDENT | The surveyor comments indicate that the odometer is not working due to the accident, the RC VIN and VIN number were verified, and the insurer is advised to check the actual driver and date of loss an… | 0.75 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | f398e4f6-30b5-5ee4-8fd2-1d2e93905d30, 95f82381-f5b9-549e-b58f-29180d700f40, ea9f785f-6bec-518b-b79d-52461b131d34 |  | 2 |
| bd9c8cdc-af13-4cf0-be8a-f00587c825b8 | INCIDENT | The description of loss is: while the insured vehicle was proceeding on its way, in the process to save a third-party motorcyclist, the insured vehicle dashed with a divider from the front side there… | 0.80 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 14033659-c0a7-557b-aaaf-e195d427175a, 59ff3ac1-d8ff-5194-a3ef-c7c78fef9a07 |  | 1 |
| f51b8653-78a9-4cb7-af4b-0c334c5e8868 | CLAIM_DETAIL | The survey report status is FSR Generated. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 8e00dc56-7a54-597b-a2d1-3c685b0418fb |  | 0 |
| dfbfc2e3-3309-4bb4-b278-f5ebb550d381 | DATE_TIME | The date of survey is 2023-08-12. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 8e00dc56-7a54-597b-a2d1-3c685b0418fb, e2a8df6a-fb79-5669-a802-ffb732357e30 |  | 1 |
| 97cc8c43-6255-42f2-b3a9-f1be9b1bdeb4 | DATE_TIME | The date of survey allotment is 2023-08-10. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | e3f43238-204a-5ab5-bb5e-a0e84bf065aa, 8e00dc56-7a54-597b-a2d1-3c685b0418fb |  | 1 |
| 4a40c113-ef6c-485a-b72c-fe113740124b | DATE_TIME | The claim registration date is 2023-08-10. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | e3f43238-204a-5ab5-bb5e-a0e84bf065aa, 8e00dc56-7a54-597b-a2d1-3c685b0418fb |  | 1 |
| 22975546-23a0-444e-8299-25236ffbb843 | DATE_TIME | The date of loss is 2023-08-08. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 8e00dc56-7a54-597b-a2d1-3c685b0418fb, 9127bdf1-9bf6-5593-95ef-b39d8bc439d8 |  | 1 |
| 18b6ccba-c2d6-4a0f-9690-a3191c334a4f | PERSONAL_INFO | The driving license type is Permanent. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 9edf3536-1633-5cc1-88b2-7cc328b01bee |  | 1 |
| 1addf99a-6590-4a61-acce-4eb46e8e42a5 | LOCATION | The driving license issuing authority is SURAT. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | e4d4cd68-700a-51fa-a53a-798a0bf87c42, 9edf3536-1633-5cc1-88b2-7cc328b01bee |  | 1 |
| eb06f630-17b7-4844-bb6c-9a9c0daa11de | DATE_TIME | The driving license date of expiry is 2026-04-11. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 9edf3536-1633-5cc1-88b2-7cc328b01bee, ebd98e06-afc4-5c5b-aff9-7890234ce307 |  | 1 |
| 84a05ab3-8612-4613-82cc-79d704b6b886 | DATE_TIME | The driving license date of issue is 2008-04-15. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 9edf3536-1633-5cc1-88b2-7cc328b01bee, 4e4cc9e0-a87a-5728-9602-ebb13dea86ae |  | 1 |
| 73ee2fa5-25e7-4ef2-92c1-373fb1bfaafb | PERSONAL_INFO | The driving license number is GUJ0510281370. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 94341b74-9c5d-5d98-b8b6-18a1ddcfcd89, 9edf3536-1633-5cc1-88b2-7cc328b01bee |  | 1 |
| 4c89b54c-598d-4724-abdc-074757c8844f | RELATIONSHIP | The driver's relation with the policy holder is Friend. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 9edf3536-1633-5cc1-88b2-7cc328b01bee |  | 2 |
| baf616fe-9655-4f3d-804f-2144c644310f | PERSONAL_INFO | The driver name is PRAKASHBHAI CHAUDARY. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | f398e4f6-30b5-5ee4-8fd2-1d2e93905d30, 9edf3536-1633-5cc1-88b2-7cc328b01bee |  | 1 |
| de062537-7987-497d-a096-324fb693555e | VEHICLE_INFO | The vehicle odometer reading is 123. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 2a641d7b-69e4-40f2-9a8a-1225be705e37 | VEHICLE_INFO | The vehicle is registered as a Private Car. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 1fb89263-3581-5618-b532-a54f9847e76d |  | 1 |
| 3ea2e20a-78ae-44bf-ad6b-17642cad71f9 | VEHICLE_INFO | The vehicle color is Metallic. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 1fb89263-3581-5618-b532-a54f9847e76d |  | 1 |
| 8762fadb-3a30-4971-ad35-168243b73b02 | VEHICLE_INFO | The vehicle manufacture year is 2013. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 1fb89263-3581-5618-b532-a54f9847e76d |  | 1 |
| fa7746f5-8c6e-4d8b-8e98-c9f1619aec36 | DATE_TIME | The vehicle registration date is 2013-10-17. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 1fb89263-3581-5618-b532-a54f9847e76d, c02a37d8-80bc-59c7-8a0e-83468bdfcfb7 |  | 1 |
| dceddc44-2f0d-482b-a5c1-1c241d53d36b | VEHICLE_INFO | The vehicle make is HYUNDAI. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 1fb89263-3581-5618-b532-a54f9847e76d |  | 1 |
| 58323a17-b869-40b3-870f-7b90f9320901 | PERSONAL_INFO | The repairer name is NAVJIVAN MOTORS PVT LTD. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 77ace883-2580-59b8-96a4-9fa8a4772739, fbf8b652-91f5-5e43-8e37-560d0439a2e7 |  | 1 |
| bc0c2348-ee1b-4bbd-8cb2-a5ecc99c215d | LOCATION | The customer address is NANA VARACHHA HOUSING SOCIETY, NANA VARACHHA DHAL, NANA VARACHHA, KAM-REJ ROAD, SURAT CITY, SURAT, GUJARAT 395006. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | e4d4cd68-700a-51fa-a53a-798a0bf87c42, 9edf3536-1633-5cc1-88b2-7cc328b01bee, 2c7687e0-fd5d-5b57-991a-ef60d15f3d3b (+1 more) |  | 1 |
| b35bd57b-6421-4e56-85a5-5a6e2c1e0b1c | PERSONAL_INFO | The customer mobile number is +919773228144. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | def02f4a-eb5b-515c-8845-d2d5ae5cb17b, 2c7687e0-fd5d-5b57-991a-ef60d15f3d3b |  | 1 |
| 458371f6-e833-427d-b302-1e55c7af6f57 | PERSONAL_INFO | The customer telephone number is +919773228144. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | def02f4a-eb5b-515c-8845-d2d5ae5cb17b, 2c7687e0-fd5d-5b57-991a-ef60d15f3d3b |  | 1 |
| 66150157-c9ef-473d-a254-5e616d45cfd3 | PERSONAL_INFO | The insured customer name is MAHESHKUMAR VASAVA. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 95f82381-f5b9-549e-b58f-29180d700f40, 2c7687e0-fd5d-5b57-991a-ef60d15f3d3b |  | 1 |
| f53eb0c9-ea3c-438e-95b9-0b0697c7c6c5 | DATE_TIME | The policy expiry date is 2024-08-02. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 8e00dc56-7a54-597b-a2d1-3c685b0418fb, d9c30ebd-9db8-5960-8cdd-c7858b4077fe |  | 1 |
| 3fe09967-e9f2-4761-bcf0-618c92b79c73 | DATE_TIME | The policy inception date is 2023-08-03. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 8e00dc56-7a54-597b-a2d1-3c685b0418fb, 17a93e4b-857c-5d00-afa1-9019522d3c40 |  | 1 |
| 3dc13ee8-9c5e-42e3-8688-991109342917 | CLAIM_DETAIL | The policy number is OC-24-2203-1801-0006512. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 8e00dc56-7a54-597b-a2d1-3c685b0418fb, 9c07b425-0de6-5ca8-b3d5-5cc63bccb8aa |  | 1 |
| 3f80d071-69e4-40c2-b69a-d82be0d2dc46 | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 1fb89263-3581-5618-b532-a54f9847e76d, 59ff3ac1-d8ff-5194-a3ef-c7c78fef9a07 |  | 1 |
| 6dfb7f45-f7bd-464e-abe4-f3b7f6c94e8d | CLAIM_DETAIL | The claim number is OC-24-2203-1801-00002660. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 8e00dc56-7a54-597b-a2d1-3c685b0418fb, bd1bb17d-05dd-5e5d-b7ee-66363a1dc6de |  | 1 |
| cdaac0aa-942d-4380-903d-5f9fe6a233b3 | VEHICLE_INFO | The vehicle engine number is G3-1ADM199755. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report | 1fb89263-3581-5618-b532-a54f9847e76d, 955daabe-5799-5646-9365-5d6af91640f6 |  | 1 |
| 42eb51d9-d6a4-474a-a21a-9412634f7abd | VEHICLE_INFO | The vehicle model is EON. | 0.95 | 223237590_Signed_Licensed_Surveyor_Report.pdf / 223237590_Signed_Licensed_Surveyor_Report / accident_report |  |  | 1 |
| 19ef15cc-9c87-47df-8b00-d9a09ac8abb1 | LOCATION | The registered office of Bajaj Allianz is at Bajaj Allianz House, 4106 Navi Vasahat, Pune - 411006. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | ee17390e-7f87-5851-8a41-70f50b02111a |  | 1 |
| ef75e9f5-2cf0-4e10-a255-cdbf37a3ea8e | CLAIM_DETAIL | The claimant is requested to provide clarification within seven days of the letter date. | 0.85 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | ee17390e-7f87-5851-8a41-70f50b02111a, 1393821b-a910-5a73-b5c8-971af0c88964 |  | 1 |
| 3339e0b7-090a-42ce-8511-8a2ca0af5985 | CLAIM_DETAIL | The insurer reserves all rights under the policy. | 0.80 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 8ed26826-f591-5c2b-9991-502a43e8ad4e |  | 1 |
| 760d51cd-c9be-4e45-87c6-c8002e78f961 | CLAIM_DETAIL | The grievance redressal procedure is available at https://www.bajajallianz.com/about-us/customer-service.html. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 1393821b-a910-5a73-b5c8-971af0c88964, 1c61ffa3-79b0-5ef9-b972-0335533888a4 |  | 0 |
| 24839594-bdcd-451d-acfa-982f551a6c6a | CLAIM_DETAIL | The barcode number on the document is RG289062596IN. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 9716903f-e9a8-5ddd-b1ad-0965d04ae9bd |  | 1 |
| 87f7966c-0a0b-459c-8562-0c4cd92246bc | CLAIM_DETAIL | The Corporate Identification Number (CIN) of Bajaj Allianz is U66010PN2000PLC015329. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 3ac7b9f2-31d4-5fd8-8514-0c5943d046a5 |  | 1 |
| 86e7132a-090b-4052-b063-792ad736f206 | PERSONAL_INFO | The insurer's website is www.bajajallianz.com. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 1c61ffa3-79b0-5ef9-b972-0335533888a4 |  | 1 |
| 6cf4b42a-7db1-458e-aa1b-5a762e86fabc | PERSONAL_INFO | The insurer's email contact is bagshelp@bajajallianz.co.in. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 1c61ffa3-79b0-5ef9-b972-0335533888a4 |  | 1 |
| 02c18fda-3df8-48b0-a631-8ca6163ce5aa | LOCATION | The insurer's office is located at 4th Floor, Atlantis Heritage, B/H Atlantis Heights, Opp. Swagat Petrol Pump, Sarabhai Main Road, Vadodara - 390007. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 1c61ffa3-79b0-5ef9-b972-0335533888a4, dcf67340-9f34-5219-bd2d-c12a7573d3ad, eb026812-1eec-54ca-b0b4-72b0f3ba41ba |  | 1 |
| 7d7ba8b5-02cc-4383-b472-0236e60ab403 | CLAIM_DETAIL | The insurer is Bajaj Allianz General Insurance Co. Ltd. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 26fb9644-4a9d-5c9d-9790-b8fa39e9d66e, eb026812-1eec-54ca-b0b4-72b0f3ba41ba |  | 1 |
| f16de011-925a-420a-ac0a-47882ce42fa4 | DATE_TIME | The letter issue date is 2023-08-18. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 7e279ee9-ec1a-5988-a3b9-feec8a4e9834, eb026812-1eec-54ca-b0b4-72b0f3ba41ba |  | 1 |
| 141f2516-b8bb-4aa6-9575-145ab12fd4f8 | PERSONAL_INFO | The insured name is Mr. Maheshwaram Indrasingh Vasava. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | c3929361-947c-5cfb-925b-52c6ecdcdc84, 47cb604a-1c29-50b7-a520-c35e00da6ab1 |  | 1 |
| 2f26c107-9267-43d5-b693-a626467baa3c | CLAIM_DETAIL | The policy number is OC-2L-3207-1801-2660. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 8ed26826-f591-5c2b-9991-502a43e8ad4e, 69467a96-1bb1-5ad7-a93e-0ae522c64988 |  | 1 |
| fc584dba-fda0-4b42-9f99-8074c195ba75 | CLAIM_DETAIL | The claim number is OC-24-2218-1801-005412. | 0.95 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 69467a96-1bb1-5ad7-a93e-0ae522c64988, 3ac8420d-a7b6-5b2e-a983-73ddc795edd7 |  | 1 |
| e22275f9-c982-4d45-9e48-1023ddfb6727 | INCIDENT | According to the insurer's assessment, the vehicle was not thrown at the time of the accident. | 0.85 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | 1393821b-a910-5a73-b5c8-971af0c88964 |  | 1 |
| a61a66e3-5d7c-4e11-901f-f6d8bb24c350 | CLAIM_DETAIL | The RDA (Registered Designated Authority) has approved the claim report. | 0.80 | 223404609_Follow-up_Letters.pdf / 223404609_Follow-up_Letters / correspondence | ee17390e-7f87-5851-8a41-70f50b02111a |  | 1 |
| 8360fc8e-4397-4398-aafd-72ccab9a54a7 | LEGAL | The letter includes a without-prejudice clause and a rights reservation statement. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | fae5ecf5-379b-56b1-931f-5402dfb28ba6 |  | 1 |
| 868e3476-b12d-4448-bc0e-9a8fc483ae76 | DATE_TIME | The letter references a prior letter dated 2023-09-19. | 0.90 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | fae5ecf5-379b-56b1-931f-5402dfb28ba6 |  | 1 |
| fc05e994-a4c8-4617-abf9-c40595d73316 | CLAIM_DETAIL | The insurer's 24-hour toll-free call center number is 1800-209-5858. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | cd0e0146-96e6-5a7b-99e8-ec339d18a82b, 18c8d7dc-a3cb-5861-908a-1df1bd2a2983 |  | 2 |
| 03e0475c-9f16-425d-b364-59711da85521 | CLAIM_DETAIL | The insurer's missed call number is 8308943060. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | cd0e0146-96e6-5a7b-99e8-ec339d18a82b, bcb1c49e-d3ad-52e6-b3b9-d5b8c7b0ac2a |  | 2 |
| 5eba6e7c-06fd-4c54-9c16-65b2ee631cf7 | CLAIM_DETAIL | The insurer's WhatsApp contact number is +917507245858. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | cd0e0146-96e6-5a7b-99e8-ec339d18a82b, e3c56b84-1c19-5347-b584-c03300c68ed1 |  | 2 |
| b981de61-862c-4cdf-92c0-2570eb56cbd1 | CLAIM_DETAIL | The insurer's corporate identification number (CIN) is U66010PN2000PLC015329. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 0ddaf7f5-f141-56c4-aeef-4a877e1f04bc |  | 2 |
| 81331896-b7a6-4576-85b9-caaae2cac0a6 | LOCATION | The insurer's office address is Bajaj Allianz General Insurance Company Ltd., 4th Floor, Atlantis Heritage, Behind Atlantis Heights, Opp Swagat Petrol Pump, Sarabhai Main Road, Vadodara – 390007 Guja… | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 4d13cbab-4b27-5ce7-abe5-7690a79d4ac9, dfddab32-b8e4-5e51-b4fa-a248fbf0824e |  | 2 |
| 3f3263b7-11d3-4d30-916a-f7edd09abb97 | LOCATION | The insurer's registered office is Bajaj Allianz House, Airport Road, Yerawada, Pune - 411006 (India). | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | ef85323f-97be-5066-8121-d8865bbb3d64, dfddab32-b8e4-5e51-b4fa-a248fbf0824e |  | 2 |
| 0d31f11b-ed81-48e4-a553-0ecf92aee299 | CLAIM_DETAIL | The insurer's IRDAI registration number is 113. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 7f71b964-2429-51ec-b964-bdad4803384d |  | 2 |
| aa60b141-7b7a-4a28-ae7a-8d7c00b664ca | CLAIM_DETAIL | The insurer is Bajaj Allianz General Insurance Company Limited. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 63d96f49-18b8-5f29-afa1-3f35f88754a9, dfddab32-b8e4-5e51-b4fa-a248fbf0824e |  | 1 |
| 44047999-9711-4acb-83de-988eb4cb6a97 | PERSONAL_INFO | The signatory's mobile number is +919898994381. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | cd0e0146-96e6-5a7b-99e8-ec339d18a82b, 9a1e46ca-ff38-56b7-b09c-ebf9f2652a79 |  | 2 |
| 4e50a004-62df-4f27-b2fd-4534d678d992 | PERSONAL_INFO | The signatory's landline number is 0265-3960861. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 10c5d622-adbc-5001-9ebd-fc2645434e62, cd0e0146-96e6-5a7b-99e8-ec339d18a82b |  | 2 |
| d12e36f7-6eee-4e83-b30f-7161f19a9451 | PERSONAL_INFO | The signatory is Bipin Shiroya, Manager. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | f993cf8f-5397-50d9-93e9-20778721f077, dfddab32-b8e4-5e51-b4fa-a248fbf0824e |  | 1 |
| 1c69daaf-8292-4f1b-8dd6-9659c00ab346 | CLAIM_DETAIL | The repudiation reason is that the insured failed to respond with clarification submission and proper documentary evidences as per requirement for further review of the claim. | 0.90 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | fae5ecf5-379b-56b1-931f-5402dfb28ba6 |  | 1 |
| f45d6bfc-d8d7-48c6-9ea3-d47cc1a9bfcf | CLAIM_DETAIL | The claim has been repudiated as final repudiation. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | fae5ecf5-379b-56b1-931f-5402dfb28ba6 |  | 1 |
| 4618777f-9cfd-4dee-a535-e14f95732bfa | PERSONAL_INFO | The claimant's phone number is +919537436355. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | fc52f242-75a1-5046-b841-9079385e023b, 436f15e1-88eb-59a3-9fa9-5decda2fa709 |  | 2 |
| 11e077f1-3590-4079-a386-8898c2c268f5 | PERSONAL_INFO | The claimant's address is 6 Nana Varachha Housing Society, Nana Varachha Dhal., Kamrej Road, Surat City, Surat, Gujarat-395006. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 3629fc10-2c04-5e9f-87b9-b96bae2e1d21, fc52f242-75a1-5046-b841-9079385e023b |  | 2 |
| d58fb330-d8b5-418e-9317-b8bd8d54f1f8 | DATE_TIME | The repudiation letter date is 2023-09-21. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | fae5ecf5-379b-56b1-931f-5402dfb28ba6 |  | 1 |
| 65d3b464-4034-4391-ae08-eba6643e1c34 | DATE_TIME | The intimation date is 2023-08-10. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 1a814bd7-078f-5de2-b9a8-5e0138682e14 |  | 1 |
| 2fe9e1e9-4e74-4809-9758-b10ce7c43081 | DATE_TIME | The loss date is 2023-08-08. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 1a814bd7-078f-5de2-b9a8-5e0138682e14 |  | 1 |
| 43f0016c-793f-468a-a783-5099816eba83 | VEHICLE_INFO | The vehicle registration number is GJ27AA0736. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 1a814bd7-078f-5de2-b9a8-5e0138682e14, d7182016-69d5-52a4-8760-0fb50a60a5fc |  | 1 |
| 8cdcacee-1ce7-45ca-9672-c1e3fd38a9ad | PERSONAL_INFO | The insured name is Mr. Maheshkumar Indrasing Vasava. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | bf893b83-6997-5c22-9df6-0e93ba387ba6, 1a814bd7-078f-5de2-b9a8-5e0138682e14, fc52f242-75a1-5046-b841-9079385e023b |  | 1 |
| f1f7816d-fea8-42d5-8a8e-e1620b90c7e5 | CLAIM_DETAIL | The policy number is OG-24-2203-1801-00005412. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | 1a814bd7-078f-5de2-b9a8-5e0138682e14, 3dbe1b3e-8c87-53f0-88a3-1e0152f2c279 |  | 1 |
| c581fbad-b600-4eb8-bb2f-850ffe76399f | CLAIM_DETAIL | The claim number is OC-24-2203-1801-00002660. | 0.95 | 223721550_Follow-up_Letters.jpg / 223721550_Follow-up_Letters / correspondence | ec3ac075-75fa-5830-a8aa-eb5b9597204a, 1a814bd7-078f-5de2-b9a8-5e0138682e14 |  | 1 |

## E — Contradictions

Total contradictions: **13**

| contradiction_id | type | severity | fact_1 (text / doc) | fact_2 (text / doc) | detection | explanation |
| --- | --- | --- | --- | --- | --- | --- |
| a8f7369c-8aab-4b74-9966-7552dfc160fe | MULTI_VALUE_SLOT | HIGH | The customer name is Mahesh Khoei Vasava. ↩ doc 218890965_Repair_Estimate | The claimant's address is 6 Nana Varachha Housing Society, Nana Varachha Dhal., Kamrej Road, Surat City, Surat, Gujarat-395006. ↩ doc 223721550_Follow-up_Letters | deterministic role-bucketing | 2 distinct values for PERSON/claimant: 'mahesh khoei vasava', 'maheshkumar indrasing vasava'. A single claim should expose exactly one claimant person.  Fact 1: The customer name is Mahesh Khoei Vasa… |
| 2ba13a48-1249-4a7c-b387-56328a17a3dc | MULTI_VALUE_SLOT | HIGH | The policy number is OG-24-2203-1801-00005412. ↩ doc 223721550_Follow-up_Letters | The policy number is OG-24-2203-1801-00006412. ↩ doc 223233267_Signed_Licensed_Surveyor_Report | deterministic role-bucketing | 3 distinct values for IDENTIFIER/policy: 'og-24-2203-1801-00005412', 'og-24-2203-1801-06005412', 'og-24-2203-1801-00006412'. A single claim should expose exactly one policy identifier.  Fact 1: The p… |
| 70f07c52-83e7-49d6-a2e7-d8c314ddc193 | MULTI_VALUE_SLOT | HIGH | The insured name is MAHESHKUMAR INDRASING VASAVA. ↩ doc 218891028_Policy_Copy | The insured name is Mr. Maheshwaram Indrasingh Vasava. ↩ doc 223404609_Follow-up_Letters | deterministic role-bucketing | 4 distinct values for PERSON/insured: 'maheshkumar indrasing vasava', 'maheshkumar vasava', 'am e3 h hdyar', 'maheshwaram indrasingh vasava'. A single claim should expose exactly one insured person. … |
| 6ab358d9-ba9f-4abd-a216-19feed4c2fd4 | MULTI_VALUE_SLOT | HIGH | The company PAN is AABCB5730G. ↩ doc 218891028_Policy_Copy | The surveyor's PAN is AJAPD3623K. ↩ doc 223233211_Supplier_Bill | deterministic role-bucketing | 4 distinct values for IDENTIFIER/pan: 'aabcb5730g', 'botpv1228n', 'botpv1128n', 'ajapd3623k'. A single claim should expose exactly one pan identifier.  Fact 1: The company PAN is AABCB5730G. Fact 2: … |
| b4137469-fd69-4b00-8184-bbe119dc2bf3 | MULTI_VALUE_SLOT | HIGH | The engine number is G3HADM199755. ↩ doc 218891028_Policy_Copy | The vehicle engine number is G3-1ADM199755. ↩ doc 223237590_Signed_Licensed_Surveyor_Report | deterministic role-bucketing | 5 distinct values for IDENTIFIER/engine: 'g3hadm199755', 'g3hadm199', 'g3h4dm199755', 'g3jh0m199756', 'g3-1adm199755'. A single claim should expose exactly one engine identifier.  Fact 1: The engine … |
| ea11e067-96b6-4dc9-ad88-f9133521437d | MULTI_VALUE_SLOT | HIGH | The chassis number is MALA351ALDM226944. ↩ doc 218891028_Policy_Copy | The vehicle chassis number is MALA351AL0R226944. ↩ doc 219430367_Pre_Inspection_Photographs_Reports | deterministic role-bucketing | 3 distinct values for IDENTIFIER/chassis: 'mala351aldm226944', 'malasiyalda226944', 'mala351al0r226944'. A single claim should expose exactly one chassis identifier.  Fact 1: The chassis number is MA… |
| 6d0553ae-f5a2-49e1-8be9-a9ab8445cdf9 | MULTI_VALUE_SLOT | HIGH | The incident date is 2023-08-19. ↩ doc 222633187_Statement_of_Driver | The date of loss is 2023-08-06. ↩ doc 223233211_Supplier_Bill | deterministic role-bucketing | 3 distinct values for DATE/incident_date: '2023-08-19', '2023-08-08', '2023-08-06'. A single claim should expose exactly one incident_date date.  Fact 1: The incident date is 2023-08-19. Fact 2: The … |
| 21c6f2cf-bd61-4636-82da-99ebcd451c1b | MULTI_VALUE_SLOT | HIGH | The claim reference number is OC-24-2203-1801-00002660. ↩ doc 222696526_Statement_of_Insured | The claim number is OC-24-2203-1801-00002600. ↩ doc 223233211_Supplier_Bill | deterministic role-bucketing | 2 distinct values for IDENTIFIER/claim: 'oc-24-2203-1801-00002660', 'oc-24-2203-1801-00002600'. A single claim should expose exactly one claim identifier.  Fact 1: The claim reference number is OC-24… |
| 8418c2c2-7299-4a40-a3c9-a5de61fed1e6 | MULTI_VALUE_SLOT | HIGH | The driver name is Prakashbhai Chaudhari. ↩ doc 223215102_Investigation_Report | The driver name is PRAKASHBHAI CHAUDARY. ↩ doc 223237590_Signed_Licensed_Surveyor_Report | deterministic role-bucketing | 3 distinct values for PERSON/driver: 'prakashbhai chaudhari', 'fir hadi h hdyar ishahdi', 'prakashbhai chaudary'. A single claim should expose exactly one driver person.  Fact 1: The driver name is P… |
| 34bc4fad-4f87-4156-ab07-72f8764d3126 | ENTITY_MISMATCH | HIGH | The company PAN is AABCB5730G. ↩ doc 218891028_Policy_Copy | The surveyor's PAN is AJAPD3623K. ↩ doc 223233211_Supplier_Bill | LLM | Four distinct PAN numbers detected: 'AABCB5730G', 'BOTPV1228N', 'BOTPV1128N', and 'AJAPD3623K'. While company and surveyor PANs are legitimately different entities, the presence of four distinct PANs… |
| 60a80973-a722-4924-8ba4-fa258245ed1b | VEHICLE_MISMATCH | HIGH | The chassis number is MALA351ALDM226944. ↩ doc 218891028_Policy_Copy | The vehicle chassis number is MALA351AL0R226944. ↩ doc 219430367_Pre_Inspection_Photographs_Reports | LLM | Three distinct chassis numbers detected: 'MALA351ALDM226944', 'MALASIYALDA226944', and 'MALA351AL0R226944'. The variations (ALDM vs AL0R vs ASIYALDA) are substantive differences, not OCR errors. A ve… |
| ab7eff0a-c321-4279-9955-3b59ebce1f85 | DATE_MISMATCH | HIGH | The incident date is 2023-08-19. ↩ doc 222633187_Statement_of_Driver | The date of loss is 2023-08-06. ↩ doc 223233211_Supplier_Bill | LLM | Three distinct incident dates detected: '2023-08-19', '2023-08-08', and '2023-08-06'. These represent a 13-day span (Aug 6 to Aug 19). An accident occurs on exactly one date. This fundamental timelin… |
| 9a98c9cc-c560-4b65-a60f-731480cde3c3 | IDENTITY_CONFLICT | HIGH | The driver name is Prakashbhai Chaudhari. ↩ doc 223215102_Investigation_Report | The driver name is PRAKASHBHAI CHAUDARY. ↩ doc 223237590_Signed_Licensed_Surveyor_Report | LLM | Three distinct driver names detected: 'Prakashbhai Chaudhari', 'PRAKASHBHAI CHAUDARY', and 'FIR HADI H HDYAR ISHAHDI'. While 'Chaudhari' vs 'Chaudary' could be a spelling variant, the presence of 'FI… |

## F — Triggered rules

Total triggered rules: **6**
Codes flagged `ORIGIN UNKNOWN`: **0**

| rule_code | rule_name | severity | code origin | evidence.text | cited fact_ids → fact texts | evidence.field_ids | evidence.claim_data_keys | source_document_ids | row_uuid |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DOC_001 | Missing Critical Documents | HIGH | FRAUD_RULES dict @ src/sqc/tools/rules.py:70 | Missing documents: RC_BOOK |  |  |  | f37435ba-8179-4121-802f-3e350153c946, 29fa1b55-1725-4bf7-a89a-8bbe207b0885, 0ac1836a-a639-4e52-9b0f-e7d5171d597f, ee46df0a-c0e7-4b53-a91c-c85070d063f5, 069cc350-c68a-4f95-a341-4137e2e81ae1, f27c5c1c-… | 4587f137-1077-4793-8ec5-fcea3515a463 |
| INC_003 | Vague Incident Description | MEDIUM | FRAUD_RULES dict @ src/sqc/tools/rules.py:252 | The claim data contains multiple null/missing critical fields: policy_number is null, claim_amount is null, and incident_date is null. These are fundamental incident details required for claim proces… |  |  | claim_id, claim_type |  | b175413a-3099-41fb-a553-d3c4e7c7801e |
| OD-TRIG-003-01 | 15 lakh Reserve in Four Wheeler | HIGH | src/sqc/rules/definitions/od_triggers.csv:23 | Vehicle is a four-wheeler (Hyundai EON SPORTZ) manufactured in 08/2013 and registered on 2013-10-17, making it approximately 11 years old. The vehicle age exceeds typical thresholds for high reserve … | [6dd84fde] The vehicle was registered on 2013-10-17. ↩ doc 218890832_Registration_Certificate; [19ee9e0b] The vehicle manufacturing month and year is 08/2013. ↩ doc 218890832_Registration_Certificate… |  | claim_id, claim_type | f37435ba-8179-4121-802f-3e350153c946 | 73c8e78d-3645-4b92-be5b-3ead2f5150d8 |
| OD-TRIG-010-01 | High Odometer Reading | MEDIUM | src/sqc/rules/definitions/od_triggers.csv:86 | The odometer reading at the time of accident is 1,05,000 km for a vehicle manufactured in 08/2013 (approximately 11 years old). This translates to roughly 9,545 km per year, which is relatively low u… | [e8e0e5c5] (fact text not found); [19ee9e0b] The vehicle manufacturing month and year is 08/2013. ↩ doc 218890832_Registration_Certificate |  | claim_id, claim_type | f37435ba-8179-4121-802f-3e350153c946 | ca01d868-1f6e-4b52-8dd7-81f15bfd750b |
| OD-TRIG-030-01 | Vehicle Age more than 5 years | MEDIUM | src/sqc/rules/definitions/od_triggers.csv:139 | Vehicle was manufactured in 08/2013 and registered on 2013-10-17, making it over 10 years old. This requires checks on road worthiness, owner count, and IDV. | [6dd84fde] The vehicle was registered on 2013-10-17. ↩ doc 218890832_Registration_Certificate; [19ee9e0b] The vehicle manufacturing month and year is 08/2013. ↩ doc 218890832_Registration_Certificate |  | claim_id, claim_type | f37435ba-8179-4121-802f-3e350153c946 | 744a64f8-7f5a-47b1-9576-d5809a9e0818 |
| OD-TRIG-041-01 | FA_Loss making vehicle \|  \| Def: 5+ Year old vehicle , claiming 75% of IDV | HIGH | src/sqc/rules/definitions/od_triggers.csv:181 | Vehicle is 11+ years old (manufactured 08/2013, registered 2013-10-17). This is a 4-wheeler (Hyundai EGH Sportz) that exceeds the 5+ year threshold for loss-making vehicle investigation. However, cla… | [19ee9e0b] The vehicle manufacturing month and year is 08/2013. ↩ doc 218890832_Registration_Certificate; [6dd84fde] The vehicle was registered on 2013-10-17. ↩ doc 218890832_Registration_Certificate… |  | claim_id, claim_type | f37435ba-8179-4121-802f-3e350153c946 | f4f816b1-ea63-4054-89b8-8e847479ce53 |

**Rule-code origin sources searched:** static `FRAUD_RULES` dict in `src/sqc/tools/rules.py`, plus the two CSV trigger files (`src/sqc/rules/definitions/od_triggers.csv` and `tp_triggers.csv`). Any rule_code not found in either source is flagged above as `ORIGIN UNKNOWN — LLM-generated?`. The pipeline does NOT ask the LLM to invent codes; an unknown here would indicate a code drift and should be investigated.

## G — Questions

Total questions: **12**

| question_id | priority | target | question_text | linked_contradiction_id (→ type / explanation) | linked_rule_code | origin |
| --- | --- | --- | --- | --- | --- | --- |
| 6ecac266-c5f0-44fa-9fa4-7e2c50e3d65a | HIGH | CLAIMANT | The claim documents show multiple variations of the claimant's name: 'Mahesh Khoei Vasava' and 'Maheshkumar Indrasing Vasava'. Please provide a government-issued ID (Aadhaar/PAN card) to confirm the … | a8f7369c-8aab-4b74-9966-7552dfc160fe  MULTI_VALUE_SLOT — 2 distinct values for PERSON/claimant: 'mahesh khoei vasava', 'maheshkumar indrasing vasava'. A single claim should expose exactly one claiman… |  | contradiction |
| de8aa2b8-0f9e-4c00-83b3-1556e446b446 | HIGH | CLAIMANT | Three different policy numbers appear in the claim documents: 'OG-24-2203-1801-00005412', 'OG-24-2203-1801-06005412', and 'OG-24-2203-1801-00006412'. Which is the correct policy number under which th… | 2ba13a48-1249-4a7c-b387-56328a17a3dc  MULTI_VALUE_SLOT — 3 distinct values for IDENTIFIER/policy: 'og-24-2203-1801-00005412', 'og-24-2203-1801-06005412', 'og-24-2203-1801-00006412'. A single claim sh… |  | contradiction |
| 76f77886-2544-4e5c-8cd3-97158cd5e419 | HIGH | INSURED | The insured name appears in four different forms across documents: 'MAHESHKUMAR INDRASING VASAVA', 'Maheshkumar Vasava', 'AM E3 H HDYAR', and 'Maheshwaram Indrasingh Vasava'. Please provide the Regis… | 70f07c52-83e7-49d6-a2e7-d8c314ddc193  MULTI_VALUE_SLOT — 4 distinct values for PERSON/insured: 'maheshkumar indrasing vasava', 'maheshkumar vasava', 'am e3 h hdyar', 'maheshwaram indrasingh vasava'. … | DOC_001 | contradiction+rule |
| d0271b71-368a-4011-b982-d6958734e3d2 | HIGH | CLAIMANT | Four different PAN numbers appear in the claim documents: 'AABCB5730G', 'BOTPV1228N', 'BOTPV1128N', and 'AJAPD3623K'. Identify which PAN belongs to the claimant, which to the insured, and which to ot… | 6ab358d9-ba9f-4abd-a216-19feed4c2fd4  MULTI_VALUE_SLOT — 4 distinct values for IDENTIFIER/pan: 'aabcb5730g', 'botpv1228n', 'botpv1128n', 'ajapd3623k'. A single claim should expose exactly one pan ide… |  | contradiction |
| 912447a3-135d-4dbc-b10c-cf9edd743c7d | HIGH | CLAIMANT | Five different engine numbers are recorded: 'G3HADM199755', 'G3HADM199', 'G3H4DM199755', 'G3JH0M199756', and 'G3-1ADM199755'. Please provide the original RC book showing the correct engine number and… | b4137469-fd69-4b00-8184-bbe119dc2bf3  MULTI_VALUE_SLOT — 5 distinct values for IDENTIFIER/engine: 'g3hadm199755', 'g3hadm199', 'g3h4dm199755', 'g3jh0m199756', 'g3-1adm199755'. A single claim should e… | DOC_001 | contradiction+rule |
| 5fbed16c-fd86-462e-833e-665cd6a2bc8a | HIGH | CLAIMANT | Three different chassis numbers appear: 'MALA351ALDM226944', 'MALA351AL0R226944', and at least one other variation. Provide the original RC book and a clear photograph/rubbing of the chassis number e… | ea11e067-96b6-4dc9-ad88-f9133521437d  MULTI_VALUE_SLOT — 3 distinct values for IDENTIFIER/chassis: 'mala351aldm226944', 'malasiyalda226944', 'mala351al0r226944'. A single claim should expose exactly … | DOC_001 | contradiction+rule |
| ba34f00b-44f0-4d11-bfb0-d2bd15ad9fb1 | HIGH | CLAIMANT | The vehicle is a 2013 Hyundai EON Sportz (approximately 11 years old) with a reserve amount of 15 lakhs or more. Given the vehicle's age and depreciation, please provide a detailed breakdown of the c… |    | OD-TRIG-003-01 | rule |
| d7671e13-164f-4820-ac81-4ff360c248b8 | HIGH | CLAIMANT | The Registration Certificate (RC book) has not been submitted. This is a mandatory document for claim processing. Please provide the original RC book immediately, as it is required to verify vehicle … |    | DOC_001 | rule |
| 0894aa35-3c76-4f4c-be8e-4640b45ac57d | HIGH | CLAIMANT | Critical claim information is missing: policy number, claim amount, and incident date are all absent from the claim submission. Please provide complete details including the exact date, time, and loc… |    | INC_003 | rule |
| accaa722-4b6c-466e-8251-679c096199b4 | HIGH | CLAIMANT | The vehicle is 11+ years old (manufactured 08/2013) and appears to be claiming a significant portion of its IDV. For vehicles over 5 years old claiming 75% or more of IDV, please explain the nature a… |    | OD-TRIG-041-01 | rule |
| 620726e4-9ba3-4ed8-9945-b8d4ee12e298 | MEDIUM | INSURED | The vehicle is over 10 years old (manufactured 08/2013, registered 2013-10-17). Please provide the latest Pollution Under Control (PUC) certificate, fitness certificate if applicable, and details of … |    | OD-TRIG-030-01 | rule |
| 9170f59a-f472-4f94-ba9d-e397c9239997 | MEDIUM | CLAIMANT | The odometer reading at the time of accident is reported as 1,05,000 km for an 11-year-old vehicle (approximately 9,545 km per year). This is unusually low usage. Please provide service records, prev… |    | OD-TRIG-010-01 | rule |

## H — Entities

### H.1 — Entity list (389 entities)

| type | value | roles | source | source_doc | source_fact_id | source_field_id | resolution outcome | neo4j node id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VEHICLE | GJ27AK0736 |  | fact | 218890832_Registration_Certificate | 5aef3a07-be34-4cb5-8fd0-bf4320d6bb1f |  | MERGED | VEHICLE-a68d774e |
| DATE | 2013-10-17 |  | fact | 218890832_Registration_Certificate | 6dd84fde-f8da-4bba-9641-5796cb511975 |  | MERGED | DATE-82b53842 |
| DATE | 2028-10-16 |  | fact | 218890832_Registration_Certificate | d6130286-b5a9-4465-94d0-c1fc7bb76710 |  | MERGED | DATE-0c840f76 |
| IDENTIFIER | malasiyalda226944 | chassis | field | 218890832_Registration_Certificate |  | ab838704-e5e4-533b-a08e-d726f180481a | NEW | IDENTIFIER-1e0c884d |
| IDENTIFIER | g3h4dm199755 | engine | field | 218890832_Registration_Certificate |  | 20afd3d5-f5a7-53ff-a1fb-b0bd921822e6 | MERGED | IDENTIFIER-c7190060 |
| ORGANIZATION | hyundai motor india |  | field | 218890832_Registration_Certificate |  | c5e5ee24-ebd6-5d5a-bbb6-f8b01cb36237 | MERGED | ORGANIZATION-3cb41262 |
| VEHICLE | EGHSPORTZ08IN |  | fact | 218890832_Registration_Certificate | d658fcbc-2dd0-4827-bfa7-875a69936b92 |  | NEW | VEHICLE-d2f51fe5 |
| DATE | 2013-08 |  | fact | 218890832_Registration_Certificate | 19ee9e0b-0c7a-4a84-80e6-5b29d53b4ff6 |  | MERGED | DATE-0b388678 |
| VEHICLE | PETROL |  | fact | 218890832_Registration_Certificate | 8a23967d-87d2-46fa-ae22-e1575a4d3499 |  | MERGED | VEHICLE-05d5c912 |
| AMOUNT | 814 |  | fact | 218890832_Registration_Certificate | 895cd2cd-ad95-4e48-a86e-87356549bf1d |  | NEW | AMOUNT-6f884268 |
| VEHICLE | 3 |  | fact | 218890832_Registration_Certificate | b00d8feb-a758-43f4-a717-81451cacefbf |  | MERGED | VEHICLE-904c16d5 |
| VEHICLE | 5 |  | fact | 218890832_Registration_Certificate | 7125e88f-8d24-4af7-9ae9-ca1f08754f37 |  | MERGED | VEHICLE-5142c181 |
| AMOUNT | 1210 |  | fact | 218890832_Registration_Certificate | d24c6e90-ab6f-489b-b935-4711b1ac32e5 |  | NEW | AMOUNT-068b5cd6 |
| AMOUNT | 2380 |  | fact | 218890832_Registration_Certificate | a7d0fc69-1c02-41e0-9a99-970476d47b5f |  | NEW | AMOUNT-22f9ebfa |
| VEHICLE | EURO4 |  | fact | 218890832_Registration_Certificate | fef58a8f-574f-4f92-8712-d25a91c0e427 |  | MERGED | VEHICLE-bd74cc1a |
| PERSON | Mahesh Kumar | owner | field | 218890832_Registration_Certificate |  | f031d491-8be2-5218-a9d7-fcaeefab8dc3 | MERGED | PERSON-378d52be |
| LOCATION | 395006:c o new |  | fact | 218890832_Registration_Certificate | a06c4254-c77d-4598-8f2f-21f65dd81a4a |  | NEW | LOCATION-43598b36 |
| IDENTIFIER | og24220318010005412 | policy | field | 218890832_Registration_Certificate |  | c8945762-dbd1-5c59-b17c-87ec552485c9 | MERGED | IDENTIFIER-e9d83ad1 |
| DATE | 2023-08-03 | policy_start | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | DATE-4f582b1d |
| DATE | 2024-08-02 | policy_end | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | DATE-d7cbb46b |
| ORGANIZATION | bajaj allianz general insurance | insurer | field | 218890832_Registration_Certificate |  | e79bd31f-68e8-5ab7-bcd4-10ba696a9848 | MERGED | ORGANIZATION-dcd88b3b |
| ORGANIZATION | bajaj finance |  | fact | 218890832_Registration_Certificate | 82871375-9d0a-4e37-9250-a147bb5d12e2 |  | MERGED | ORGANIZATION-417b2cf8 |
| DATE | 2028-10-18 |  | fact | 218890832_Registration_Certificate | 61792c7c-f500-4935-b440-ad890f040f23 |  | MERGED | DATE-fa64c970 |
| AMOUNT | 200 |  | fact | 218890832_Registration_Certificate | c064a021-868e-4af8-a57e-97ac0a61f4cc |  | NEW | AMOUNT-8a678388 |
| IDENTIFIER | gj230808c9783109 |  | fact | 218890832_Registration_Certificate | 2ff81d24-caa3-4aa8-8f09-6843afa14c0c |  | MERGED | IDENTIFIER-b9bab35d |
| DATE | 2023-08-08 |  | fact | 218890832_Registration_Certificate | c017cd96-ab70-40f4-8ff6-9394199ba1a0 |  | MERGED | DATE-a30da6ea |
| AMOUNT | 20634 |  | fact | 218890832_Registration_Certificate | abe0f5e0-07b5-46a5-a61a-da61ed015efe |  | NEW | AMOUNT-275e1ba2 |
| PHONE | 9727635960 |  | field | 218890832_Registration_Certificate |  | edbd38b3-a35c-5aee-b87e-773de51ca6e3 | MERGED | PHONE-d20bb764 |
| IDENTIFIER | gj230808v2160368 |  | fact | 218890832_Registration_Certificate | 9d4fa10e-fd24-4801-90d7-ce360dd61d96 |  | MERGED | IDENTIFIER-5cc577f6 |
| VEHICLE | ACTIVE |  | fact | 218890832_Registration_Certificate | 4f9b50a6-65e5-483e-82bc-6ff710c758fa |  | MERGED | VEHICLE-e2ab73f6 |
| LOCATION | 395009:office 3rd fl |  | fact | 218890832_Registration_Certificate | 1915fb53-8702-448b-ab41-771232ae85c5 |  | MERGED | LOCATION-9e048829 |
| IDENTIFIER | gj0502813706 | driving_licence | field | 223214762_Investigation_Report |  | a254c8b3-601d-5d72-8eaf-b627f5291607 | MERGED | IDENTIFIER-e5996747 |
| DATE | 2006-04-15 |  | fact | 218890867_Motor_Driving_License_(MDL) | 9485343d-fedc-47b8-928f-644b9e507369 |  | MERGED | DATE-fe1d2d4c |
| PERSON | Chaudhari Prakashbhai Manjibhai | unknown | fact | 218890867_Motor_Driving_License_(MDL) | 9e3971b3-43d3-4666-860b-470c69b8ef1e |  | MERGED | PERSON-05c066b4 |
| LOCATION | 394540:a p balaibuva |  | fact | 218890867_Motor_Driving_License_(MDL) | 8c457bc6-0aea-4708-81d8-d81522b7909b |  | MERGED | LOCATION-e719b957 |
| DATE | 1987-09-07 |  | fact | 218890867_Motor_Driving_License_(MDL) | 25de760f-2fd3-4ab5-90d4-47c5845863e1 |  | MERGED | DATE-eca3476d |
| VEHICLE | MCEX50CCWIGR |  | fact | 218890867_Motor_Driving_License_(MDL) | f075e53a-54ba-4ef9-b02c-239dc126fb9b |  | MERGED | VEHICLE-06700753 |
| DATE | 2006-04-12 |  | fact | 218890867_Motor_Driving_License_(MDL) | 698de4b4-a254-476f-8f3d-998c56037611 |  | MERGED | DATE-d22f15c9 |
| DATE | 2026-04-11 |  | fact | 218890867_Motor_Driving_License_(MDL) | 698de4b4-a254-476f-8f3d-998c56037611 |  | MERGED | DATE-bc427431 |
| VEHICLE | LMV |  | fact | 218890867_Motor_Driving_License_(MDL) | e414e212-12e9-4b5d-91c7-aeb3371ee6cd |  | MERGED | VEHICLE-b8769466 |
| IDENTIFIER | oc249003180100002660 | policy | field | 218890910_Claim_Form |  | ed6f71e3-59b5-5452-b8e1-3e1b5c775bb9 | MERGED | IDENTIFIER-f413862e |
| PERSON | Am E3 H Hdyar | insured | fact | 218890910_Claim_Form | 3c344931-1c1c-447b-b03c-f8e7dda52359 |  | NEW | PERSON-32bf0314 |
| LOCATION | gunami vorbad |  | fact | 218890910_Claim_Form | 05aa5e1b-6bff-425b-88e6-7f0f924ca948 |  | NEW | LOCATION-01e336e0 |
| LOCATION | gunami |  | fact | 218890910_Claim_Form | 795a22de-e1e7-44b3-8186-2f1d2590fa8c |  | MERGED | LOCATION-3440f54a |
| LOCATION | 841601: |  | fact | 218890910_Claim_Form | 053513d0-650d-4dcf-a645-447ef83eb5b3 |  | NEW | LOCATION-14dea1df |
| LOCATION | bihar |  | field | 218890910_Claim_Form |  | 6d827c66-88ee-5564-a2a6-c72d4232a47d | NEW | LOCATION-9401a1b3 |
| VEHICLE | CA2AA0036 |  | fact | 218890910_Claim_Form | 3ab40841-46dc-480b-b540-648e302f2775 |  | MERGED | VEHICLE-b0a4ed09 |
| LOCATION | nema vasselley city |  | fact | 218890910_Claim_Form | 5c8d6f0f-7126-436a-b519-8304f56a13b3 |  | NEW | LOCATION-30b4b350 |
| PERSON | Fir Hadi H Hdyar Ishahdi | driver | fact | 218890910_Claim_Form | f2a755e3-6391-4763-a343-32e1531e3c9f |  | NEW | PERSON-785ef95a |
| IDENTIFIER | ujosio02hadi061 |  | fact | 218890910_Claim_Form | 76995883-fa5b-4bb4-8a57-b367b6d75cc1 |  | NEW | IDENTIFIER-51f0bf50 |
| DATE | 2025-04-10 |  | fact | 218890910_Claim_Form | 72d53dbb-0f84-4347-8f06-989b343ed57d |  | NEW | DATE-bd6244f2 |
| PERSON | Maha 3 Hdyar | signatory | fact | 218890910_Claim_Form | a5476ca6-b520-4147-a9dc-f26dfa8f58d0 |  | NEW | PERSON-dd86318c |
| ORGANIZATION | bajaj allianz |  | fact | 218890942_Claim_Form | f135206b-376c-4dee-a104-594fa1f98cee |  | MERGED | ORGANIZATION-f04d7ed5 |
| IDENTIFIER | 230 |  | fact | 218890965_Repair_Estimate | 422d3a15-fe9f-468f-a241-6452686045d1 |  | MERGED | IDENTIFIER-3e9ef6ed |
| DATE | 2023-08-09 |  | fact | 218890965_Repair_Estimate | c5d4d2b9-cbb6-43e4-9a41-8b3f8b3e25ab |  | MERGED | DATE-b9174e3b |
| VEHICLE | GJ9924AA0436 |  | fact | 218890965_Repair_Estimate | dba23968-6adc-4d84-bdb0-8d8c8bdb0f30 |  | MERGED | VEHICLE-0ad77f35 |
| VEHICLE | HYUNDAI |  | fact | 218890965_Repair_Estimate | 482cad67-1411-4de5-8657-501fdb4a6952 |  | MERGED | VEHICLE-7294b9ae |
| VEHICLE | EON |  | fact | 218890965_Repair_Estimate | 0ff9e2bf-2b8d-461f-9b03-17975af59b82 |  | MERGED | VEHICLE-b60d5ca7 |
| VEHICLE | WHITE |  | fact | 218890965_Repair_Estimate | 4adf2ff0-7ef4-4ea6-956a-abe4ab070cdc |  | MERGED | VEHICLE-764cdf62 |
| PERSON | Mahesh Khoei Vasava | claimant | fact | 218890965_Repair_Estimate | e5da41bb-cb55-4fe1-965a-951f56cac058 |  | MERGED | PERSON-6cbe5819 |
| ORGANIZATION | navjivan motors |  | field | 219032145_Job_Card |  | 8fb25af8-d434-59b1-bdf7-288aec56ef5d | MERGED | ORGANIZATION-b66529a9 |
| LOCATION | smc udhna south |  | fact | 218890965_Repair_Estimate | 72e22403-9e09-4c9c-83b7-4b4ac44fe8b0 |  | MERGED | LOCATION-bd8da89b |
| PHONE | 2613206002 |  | fact | 218890965_Repair_Estimate | 8fe90c82-1d3a-4f89-9dc9-0c26e5a81833 |  | MERGED | PHONE-1c52590c |
| EMAIL | bodyshop@navjivanhydundai.com |  | fact | 218890965_Repair_Estimate | 22d4a098-169e-4650-982c-a785f80ed38b |  | MERGED | EMAIL-7d9ff876 |
| LOCATION | tulsi krupa arcade |  | fact | 218890965_Repair_Estimate | 78fe66e4-8c97-4d0c-bbd8-5db197efd6dd |  | MERGED | LOCATION-57dcc118 |
| PHONE | 2612855777 |  | fact | 218890965_Repair_Estimate | 898c1348-f554-4e39-ae9e-9b0de53055d8 |  | MERGED | PHONE-c213449f |
| VEHICLE | FRONTBUMPER |  | fact | 218890965_Repair_Estimate | ec04abd0-f0f4-4358-b4f2-9c845e7968dd |  | MERGED | VEHICLE-45dbdd17 |
| VEHICLE | REARBUMPER |  | fact | 218890965_Repair_Estimate | 2035e227-ce7e-416d-ad26-300ff02acbaf |  | MERGED | VEHICLE-23f28641 |
| VEHICLE | LOWERGRILLE |  | fact | 218890965_Repair_Estimate | 0fdeda31-d95f-4db0-ac85-ec028ff0976f |  | MERGED | VEHICLE-832255bf |
| VEHICLE | RHFENDERS |  | fact | 218890965_Repair_Estimate | b9dad985-8526-4618-8a92-fe193c085fb8 |  | MERGED | VEHICLE-84075f29 |
| VEHICLE | LHFENDERS |  | fact | 218890965_Repair_Estimate | 0709eac0-de14-45af-8da6-4bc301fb06b9 |  | MERGED | VEHICLE-c53476bb |
| VEHICLE | HEADLIGHTER |  | fact | 218890965_Repair_Estimate | 8ab83020-728e-411a-b2cb-46af74408cc6 |  | MERGED | VEHICLE-7be127d7 |
| VEHICLE | CONDENSOR |  | fact | 218890965_Repair_Estimate | 01ab2aac-ad9e-49db-88f9-1daca197d806 |  | MERGED | VEHICLE-d5407499 |
| AMOUNT | 8000 |  | fact | 218890965_Repair_Estimate | a1abc1f2-f883-43ae-abca-c21551c8ec51 |  | NEW | AMOUNT-81fd660f |
| AMOUNT | 1000 |  | fact | 218890965_Repair_Estimate | 35207936-fcd8-4046-b5b2-0e2c1a0d29be |  | NEW | AMOUNT-e9fd11b6 |
| IDENTIFIER | og242203180100005412 | policy | field | 218891028_Policy_Copy |  | 8256265f-bda3-59c3-b052-5797d78ce904 | MERGED | IDENTIFIER-6a60df6f |
| PERSON | Maheshwaram Indrasingh Vasava | insured, unknown, claimant | field | 218891028_Policy_Copy |  | 9359f38c-16bb-539a-9156-b5378f397d1b | MERGED | PERSON-8eeb6bb0 |
| LOCATION | 395006:nana varachha housing |  | field | 223237590_Signed_Licensed_Surveyor_Report |  | 0d70393e-c059-54b1-bcc8-9c10607e178a | MERGED | LOCATION-a024ee78 |
| IDENTIFIER | 399252385 |  | fact | 218891028_Policy_Copy | 3572a04c-e89c-4f37-9ee4-5626344b8b5f |  | MERGED | IDENTIFIER-091c9df7 |
| LOCATION | gujarat |  | field | 218890832_Registration_Certificate |  | 9fcf74bb-a76b-5b27-b049-c0583008e1d3 | MERGED | LOCATION-247c8f1a |
| DATE | 2023-08-02 |  | fact | 218891028_Policy_Copy | a96b07ea-41b9-43ff-b115-83fb9a03e5df |  | MERGED | DATE-d97dfbc5 |
| IDENTIFIER | 5883382461 |  | fact | 218891028_Policy_Copy | b2e9d509-a7fa-4da7-a1d3-9370801b5f33 |  | MERGED | IDENTIFIER-f51eb407 |
| IDENTIFIER | 24aabcb5730g1z3 |  | fact | 218891028_Policy_Copy | 174ea5da-bb56-4915-93c8-f2b65d1f2f6e |  | MERGED | IDENTIFIER-6b00e638 |
| IDENTIFIER | aabcb5730g |  | fact | 218891028_Policy_Copy | 6b755373-05a5-4916-b558-3f3290d42cb4 |  | MERGED | IDENTIFIER-b3ac3197 |
| VEHICLE | GJ27AA0736 | claimant_vehicle | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | VEHICLE-b5e9f3ac |
| LOCATION | ahmedabad |  | fact | 218891028_Policy_Copy | 993e974b-bfab-4388-883f-db16f99b2727 |  | MERGED | LOCATION-d232962e |
| IDENTIFIER | g3hadm199755 | engine | field | 218891028_Policy_Copy |  | f2ac6f6b-b0b6-57e0-a383-79984bbae18e | MERGED | IDENTIFIER-e99ecf60 |
| IDENTIFIER | mala351aldm226944 | chassis | field | 218891028_Policy_Copy |  | e4796257-98c5-57c6-a475-b7dc69136521 | MERGED | IDENTIFIER-b7be51af |
| VEHICLE | SPORTZ |  | fact | 218891028_Policy_Copy | 0c5f0c97-c6ff-4f3d-9887-cc310c118dfa |  | MERGED | VEHICLE-cf2830cb |
| AMOUNT | 200000 |  | fact | 218891028_Policy_Copy | 0508a76c-00af-4b06-816b-068060e9bd70 |  | NEW | AMOUNT-d465ae9b |
| AMOUNT | 3031 |  | fact | 218891028_Policy_Copy | 15924afa-4d72-49c8-ba4a-7797cfd324db |  | NEW | AMOUNT-be782d39 |
| AMOUNT | 2094 |  | fact | 218891028_Policy_Copy | 4a0459ba-6c62-420b-9d13-cf76369e4286 |  | NEW | AMOUNT-755de994 |
| AMOUNT | 331 |  | fact | 218891028_Policy_Copy | 6b357019-3261-4068-8a6d-c01bdb915c04 |  | NEW | AMOUNT-2876177c |
| AMOUNT | 1500000 |  | fact | 218891028_Policy_Copy | 6b357019-3261-4068-8a6d-c01bdb915c04 |  | NEW | AMOUNT-36b0f057 |
| AMOUNT | 50 |  | fact | 218891028_Policy_Copy | 1aea3259-0423-4d63-b885-9ce4a630b09a |  | NEW | AMOUNT-21a0fa2f |
| AMOUNT | 250 |  | fact | 218891028_Policy_Copy | cabde65f-6fea-4dff-8432-dd88ffd867c7 |  | NEW | AMOUNT-3c56f0b1 |
| AMOUNT | 100000 |  | fact | 218891028_Policy_Copy | cabde65f-6fea-4dff-8432-dd88ffd867c7 |  | NEW | AMOUNT-f58a2b0a |
| AMOUNT | 2725 |  | fact | 218891028_Policy_Copy | 6d48527d-9a9b-4e17-ad67-c7a4c77928a6 |  | NEW | AMOUNT-e947be52 |
| AMOUNT | 5756 |  | fact | 218891028_Policy_Copy | 98aae3ec-4131-49c5-bcbc-1dbf3dcc52f4 |  | NEW | AMOUNT-5d19393a |
| AMOUNT | 518 |  | fact | 218891028_Policy_Copy | 7a3b496b-b03c-4209-af7b-9166a8fc818e |  | NEW | AMOUNT-de9c77a0 |
| AMOUNT | 6792 |  | fact | 218891028_Policy_Copy | 4b0a7122-df8d-43f6-9e18-82bd6450483b |  | NEW | AMOUNT-3fc958d2 |
| IDENTIFIER | irdan113rp00251v01200102 |  | fact | 218891028_Policy_Copy | b3644f8d-c709-47db-ab1e-eee9716ac9c7 |  | MERGED | IDENTIFIER-6f0f1791 |
| LOCATION | 395009:2nd floor citadel |  | fact | 218891028_Policy_Copy | e367e2c9-da6a-40cd-be0b-dae15645ce3d |  | MERGED | LOCATION-9bbd0dc7 |
| PHONE | 9876256882 |  | fact | 218891028_Policy_Copy | 2dd95ea0-a570-41f0-805e-d6c64297c807 |  | MERGED | PHONE-1f5d242b |
| LOCATION | 411006:bajaj allianz airport |  | fact | 218891028_Policy_Copy | 8313375a-b218-4691-a22a-2a4ac66616a6 |  | MERGED | LOCATION-b07d1283 |
| LOCATION | india |  | fact | 218891028_Policy_Copy | ab3de816-c876-495c-97e0-7b03ab7618d3 |  | MERGED | LOCATION-e9719e64 |
| IDENTIFIER | botpv1228n |  | fact | 219032034_AML_Documents | cf7063a9-6919-4e57-b7b6-ae81a27839f1 |  | MERGED | IDENTIFIER-1ce77988 |
| PERSON | Bhrikumar Indrasing Vasava | unknown | field | 219032034_AML_Documents |  | b4790284-da4f-5720-a039-71157369460f | MERGED | PERSON-3af8df65 |
| PERSON | Indrasing Divejiyabhai Vasava | unknown | field | 219032034_AML_Documents |  | b4790284-da4f-5720-a039-71157369460f | MERGED | PERSON-fc352414 |
| ORGANIZATION | income tax department |  | fact | 219032034_AML_Documents | d18cd5d6-332e-4b9a-960a-b0b5a1bef6ca |  | MERGED | ORGANIZATION-b586498f |
| IDENTIFIER | 1800 |  | fact | 219032145_Job_Card | f67bb30f-845b-47c9-8264-553fa911b757 |  | MERGED | IDENTIFIER-e5dc81ce |
| AMOUNT | 2000 |  | fact | 219032145_Job_Card | e421b101-59f9-4fe5-b9d1-e6d6ae5f7ed5 |  | NEW | AMOUNT-eb84f3e1 |
| PERSON | Vikesh Patil | unknown | field | 219032145_Job_Card |  | 540352f1-699b-5a08-a6bb-143e7835263d | MERGED | PERSON-e8384e18 |
| PHONE | 9727635980 |  | field | 219032145_Job_Card |  | 9765aed9-958f-5044-b324-ef3db07939c5 | MERGED | PHONE-8651ce64 |
| PERSON | Nana Varaziha | unknown | fact | 219032145_Job_Card | 77106c9b-b662-4a38-857b-56473c3dff2c |  | MERGED | PERSON-8896d9d9 |
| VEHICLE | GH27AA0136 |  | fact | 219032145_Job_Card | 4bd9321b-8a85-42ec-9819-5e5a9c2ee11c |  | MERGED | VEHICLE-043c757c |
| DATE | 10:45 PM |  | fact | 219032145_Job_Card | 71e5b003-bfb5-478c-ad5f-623d31ef53f7 |  | MERGED | DATE-2061c858 |
| LOCATION | surat |  | field | 218890832_Registration_Certificate |  | 54956e21-3263-5770-ad62-025471d179a0 | MERGED | LOCATION-acabe2fe |
| EMAIL | navjivanmotors@gmail.com |  | fact | 219032145_Job_Card | 9919e3b7-2852-4d52-820e-2f9cad573af5 |  | MERGED | EMAIL-25a250b3 |
| IDENTIFIER | et23080090 |  | fact | 219358654_Repair_Estimate | ee8f96cd-2612-48d2-8226-286bc7331b19 |  | MERGED | IDENTIFIER-6689c05a |
| VEHICLE | CWHITE |  | fact | 219358654_Repair_Estimate | 737e366b-446f-4f21-a603-67598676eb0e |  | MERGED | VEHICLE-f5068296 |
| DATE | 2023-08-16 |  | fact | 219358654_Repair_Estimate | 03eda4cb-92c9-4d03-93d3-844568ecfc96 |  | MERGED | DATE-a80c1996 |
| IDENTIFIER | r202305933 | claim | field | 219358654_Repair_Estimate |  | da35a6d3-5b3a-5edb-8dbb-d4cee880e790 | MERGED | IDENTIFIER-fc455f91 |
| IDENTIFIER | accidentalrepair |  | fact | 219358654_Repair_Estimate | 45266045-16ce-4903-84c4-3d77e0e66282 |  | MERGED | IDENTIFIER-526d6a9d |
| LOCATION | nana varachha housing |  | fact | 219358654_Repair_Estimate | b502c2db-bb9a-4fc5-919e-4678282a34f7 |  | MERGED | LOCATION-82d5c563 |
| AMOUNT | 112712 |  | fact | 219358654_Repair_Estimate | 2113839c-bd9d-4f08-8040-f3e81e01498d |  | NEW | AMOUNT-ffcdaf3b |
| AMOUNT | 47613 |  | fact | 219358654_Repair_Estimate | 57f71856-fa46-44de-8524-1a037d4f367c |  | NEW | AMOUNT-405d3117 |
| AMOUNT | 65099 |  | fact | 219358654_Repair_Estimate | 6c70215f-ac33-4fa5-b3dd-c2f8f0172354 |  | NEW | AMOUNT-5b4476fb |
| AMOUNT | 1024 |  | fact | 219358654_Repair_Estimate | 6b2a0d6c-0656-410d-b760-faaeb1ff5ea2 |  | NEW | AMOUNT-62234f34 |
| IDENTIFIER | 08m9886100 |  | fact | 219358654_Repair_Estimate | 6b2a0d6c-0656-410d-b760-faaeb1ff5ea2 |  | MERGED | IDENTIFIER-44802d0c |
| AMOUNT | 2602 |  | fact | 219358654_Repair_Estimate | be53cd83-d714-408a-8f4b-f9b4b528133d |  | NEW | AMOUNT-63dae61b |
| IDENTIFIER | 253104n000 |  | fact | 219358654_Repair_Estimate | be53cd83-d714-408a-8f4b-f9b4b528133d |  | MERGED | IDENTIFIER-1721497e |
| AMOUNT | 6099 |  | fact | 219358654_Repair_Estimate | d517ce67-7f5e-41af-bd37-4cb49c105752 |  | NEW | AMOUNT-85fbd7cc |
| IDENTIFIER | 495004n000 |  | fact | 219358654_Repair_Estimate | d517ce67-7f5e-41af-bd37-4cb49c105752 |  | MERGED | IDENTIFIER-ff66c115 |
| AMOUNT | 4939 |  | fact | 219358654_Repair_Estimate | a64d0fbe-1e72-4b84-b1f8-3a1b28eedda2 |  | NEW | AMOUNT-632733ed |
| IDENTIFIER | 8611105200 |  | fact | 219358654_Repair_Estimate | a64d0fbe-1e72-4b84-b1f8-3a1b28eedda2 |  | MERGED | IDENTIFIER-6a01eb86 |
| AMOUNT | 10666 |  | fact | 219358654_Repair_Estimate | dfcf5927-1a27-40d5-ae85-4aca0d50aebb |  | NEW | AMOUNT-26d6801b |
| IDENTIFIER | 977014n100 |  | fact | 219358654_Repair_Estimate | dfcf5927-1a27-40d5-ae85-4aca0d50aebb |  | MERGED | IDENTIFIER-09ceffc7 |
| AMOUNT | 944 |  | fact | 219358654_Repair_Estimate | 2e8f7311-130b-4682-98d2-ed28ba13a637 |  | NEW | AMOUNT-ee2ac129 |
| AMOUNT | 1888 |  | fact | 219358654_Repair_Estimate | 36061bfe-5e80-4de5-a52a-ceb2f388386a |  | NEW | AMOUNT-54a6c5af |
| AMOUNT | 17700 |  | fact | 219358654_Repair_Estimate | 47010556-c197-4545-8f5b-f4cabb853e8f |  | NEW | AMOUNT-b3a26e8f |
| AMOUNT | 31860 |  | fact | 219358654_Repair_Estimate | 7fec3bd9-c7b9-44de-b5ae-8b3366fe6667 |  | NEW | AMOUNT-b5407bd0 |
| AMOUNT | 1499 |  | fact | 219358654_Repair_Estimate | c57942cd-9a0b-497a-a09b-8fda58b9b4fd |  | NEW | AMOUNT-389d238f |
| IDENTIFIER | mala351al0r226944 | chassis | field | 219430367_Pre_Inspection_Photographs_Reports |  | 88bbfe1c-7017-51ec-8236-9d75c5334d2f | MERGED | IDENTIFIER-74940127 |
| IDENTIFIER | g3jh0m199756 | engine | field | 219430367_Pre_Inspection_Photographs_Reports |  | c7b6323b-12cc-5e06-8473-a8acae3c7e26 | MERGED | IDENTIFIER-c3876e59 |
| ORGANIZATION | hyundai |  | field | 219430367_Pre_Inspection_Photographs_Reports |  | 8a09c1e0-7219-53a9-8841-59ccc0a16c95 | MERGED | ORGANIZATION-eabeaa69 |
| VEHICLE | I10SPORT2BWM |  | fact | 219430367_Pre_Inspection_Photographs_Reports | d9b13a1c-e377-4bfa-9513-c32ee5b6c000 |  | MERGED | VEHICLE-ceb14d61 |
| AMOUNT | 1197 |  | fact | 219430367_Pre_Inspection_Photographs_Reports | f41e7ce3-efa9-4ecd-b2e4-6a8b63d3cca2 |  | NEW | AMOUNT-8ffeee7e |
| VEHICLE | LMVCAR |  | fact | 219430367_Pre_Inspection_Photographs_Reports | 4180c352-786d-4ba5-b3d8-4e1e0193bc7b |  | MERGED | VEHICLE-07190b9a |
| VEHICLE | NIL |  | fact | 219430367_Pre_Inspection_Photographs_Reports | 61b810db-6d1e-4091-84dc-6848e3591072 |  | MERGED | VEHICLE-21629ad2 |
| ORGANIZATION | government of gujarat |  | fact | 219430367_Pre_Inspection_Photographs_Reports | 60d84a30-3574-4055-9be3-24336519d043 |  | MERGED | ORGANIZATION-3ecc1336 |
| DATE | 2023-09-19 |  | fact | 222633146_Statement_of_Insured | 2d3e5925-fe90-43ea-94dc-504147bb5ad6 |  | MERGED | DATE-4e2a8e15 |
| PERSON | Prasann Maheshwari | signatory | fact | 222633146_Statement_of_Insured | 1d5a26d1-68d2-4ab1-b6e2-492caf686523 |  | NEW | PERSON-a1a3d7bf |
| PHONE | 919411411 |  | fact | 222633146_Statement_of_Insured | cf9ea55c-4243-4e3c-a6a8-05359e651761 |  | NEW | PHONE-65ab002a |
| IDENTIFIER | 9474625160 |  | fact | 222633146_Statement_of_Insured | d1a5d7b6-2f8f-4aef-bb25-947a0a08d730 |  | NEW | IDENTIFIER-1bae3e11 |
| DATE | 2023-08-19 | incident_date | field | 222633187_Statement_of_Driver |  | 4fb7ef04-aa4c-5dc1-ac2a-ef586101a04e | MERGED | DATE-bece97ad |
| PHONE | 8308953545 |  | field | 222633187_Statement_of_Driver |  | 4fb7ef04-aa4c-5dc1-ac2a-ef586101a04e | MERGED | PHONE-bda2e820 |
| LOCATION | front end |  | fact | 222633313_Vehicle_Damage_Photo | afc3541a-61c5-44df-afc6-cf904d69c4fd |  | NEW | LOCATION-51cec8a7 |
| LOCATION | parking lot |  | fact | 222633313_Vehicle_Damage_Photo | 5e5a39b1-d8b8-4464-bb5d-911974461b74 |  | NEW | LOCATION-02d41ee1 |
| LOCATION | surat india |  | fact | 222633407_Spot_Photo_Sketch | 7ec83d08-5171-423c-bac6-75df3b98dbb8 |  | MERGED | LOCATION-ad2a7d58 |
| ORGANIZATION | unacademy |  | field | 222633407_Spot_Photo_Sketch |  | 203a4adf-7bf4-546a-8510-46cea9479e3d | MERGED | ORGANIZATION-3b6b9d69 |
| VEHICLE | AUTORICKSHAW |  | fact | 222633407_Spot_Photo_Sketch | 5a13122b-b7eb-41f6-ae84-15b12141060e |  | MERGED | VEHICLE-724f1b2f |
| VEHICLE | MOTORCYCLESSCOOTERS |  | fact | 222633407_Spot_Photo_Sketch | 97373e6e-874d-476b-94a6-edc96ceaedd9 |  | NEW | VEHICLE-aa5e1a1d |
| PERSON | Prakashbhai Chaudhari | unknown, driver | field | 222633435_Any_Other |  | d89ebad8-d87f-586c-aae3-b7c6b2eeae9f | MERGED | PERSON-386f2308 |
| EMAIL | uahachaudhari28@gmail.com |  | fact | 222633435_Any_Other | 9b7daac3-9f7b-4f35-ab65-9015e23a5c23 |  | MERGED | EMAIL-c85da756 |
| PERSON | Maheshkumar Vasava | unknown, insured | field | 223214762_Investigation_Report |  | 64baded4-5bad-5979-800f-61e69670f0fb | MERGED | PERSON-b4bb96fd |
| EMAIL | mivasava1988@gmail.com |  | fact | 222633435_Any_Other | e6a78bc6-ef3d-456e-9096-80628161f218 |  | MERGED | EMAIL-39be9bb5 |
| ORGANIZATION | bupusiraum cabs |  | field | 222633435_Any_Other |  | ad3f340a-7c34-572c-93a2-85694fdbecf1 | MERGED | ORGANIZATION-5c967df1 |
| PHONE | 9079385368 |  | field | 222633435_Any_Other |  | 42346f7b-d5b3-5e84-93b2-757aa5085e1a | MERGED | PHONE-5149c0f0 |
| PHONE | 9913316746 |  | fact | 222633435_Any_Other | feb90b9e-38fe-4f8e-bc8d-a2b4d5c4d539 |  | MERGED | PHONE-cddfa16a |
| VEHICLE | 9227463964 |  | fact | 222633435_Any_Other | 1137ab4d-f4e7-4543-912e-4a75473d2755 |  | MERGED | VEHICLE-5a05805d |
| DATE | 2023-07-27 |  | fact | 222633435_Any_Other | 768da60e-2c79-4465-9099-a15563938dc7 |  | MERGED | DATE-c8aa0327 |
| VEHICLE | 9455504 |  | fact | 222633435_Any_Other | ebd5ceff-874a-4cef-8330-830f7741e816 |  | NEW | VEHICLE-0acc9c61 |
| AMOUNT | 1510664 |  | fact | 222633435_Any_Other | 666af635-ddcd-405f-a7d8-53bdede1fe11 |  | NEW | AMOUNT-63bd1958 |
| AMOUNT | 29950 |  | fact | 222633435_Any_Other | 9a4cfdde-ccca-4340-892a-c50004ce8e98 |  | NEW | AMOUNT-ea947805 |
| AMOUNT | 1510652 |  | fact | 222633435_Any_Other | d7d3c59c-f105-48b4-815c-d72a8a64d551 |  | NEW | AMOUNT-d40d0afc |
| AMOUNT | 149000 |  | fact | 222633435_Any_Other | d12a659b-dc2b-4730-8d0b-3e34b43e6eec |  | NEW | AMOUNT-14562954 |
| LOCATION | candu uka |  | field | 222633435_Any_Other |  | 6ce4e804-599f-5cfc-9e8b-f7d3b2343287 | MERGED | LOCATION-236a898a |
| IDENTIFIER | insuredstatement |  | fact | 222696526_Statement_of_Insured | c4288799-7d3c-4be5-b50f-1a729e5147b1 |  | NEW | IDENTIFIER-08705ded |
| PHONE | 9227637160 |  | field | 222696526_Statement_of_Insured |  | 84beac75-9e61-579e-882c-50bb1e5a6ac7 | NEW | PHONE-199da433 |
| IDENTIFIER | oc242203180100002660 | claim | field | 223214762_Investigation_Report |  | f1fc68c5-b192-5b09-bc79-f09fa212155d | MERGED | IDENTIFIER-9a6e0ba1 |
| PERSON | Mahesh Jyear | unknown | fact | 222696526_Statement_of_Insured | fc004856-8687-40c1-93c6-13b570bae640 |  | NEW | PERSON-34689b07 |
| DATE | 2023-08-10 |  | fact | 223214762_Investigation_Report | b98507b6-36c7-4083-8a0c-14c3264e5bdd |  | MERGED | DATE-3368f25b |
| DATE | 2023-08-18 |  | fact | 223214762_Investigation_Report | 10394f93-756c-4122-81b4-19c2222f8488 |  | MERGED | DATE-615c5f7d |
| DATE | 1988-09-13 |  | fact | 223214762_Investigation_Report | bf45f508-67af-40b0-a950-e7e02f1d0071 |  | MERGED | DATE-1b68caa0 |
| IDENTIFIER | botpv1128n |  | fact | 223214762_Investigation_Report | d77b0ed3-c547-4b41-a3ce-77163992c80f |  | MERGED | IDENTIFIER-81ddaebd |
| PHONE | 9773228144 |  | field | 223214762_Investigation_Report |  | 26c97d80-c093-5fc3-ab92-dd9cc03d0ef5 | MERGED | PHONE-f94eaf64 |
| ORGANIZATION | radhi lab | employer | field | 223214762_Investigation_Report |  | cafaa179-c204-502c-969c-17e342965000 | MERGED | ORGANIZATION-99a61b53 |
| IDENTIFIER | g3hadm199 | engine | field | 223214762_Investigation_Report |  | f699d483-d482-5432-b81c-ac8cb5803645 | MERGED | IDENTIFIER-6e0a0204 |
| ORGANIZATION | bappa sitaram car mela |  | field | 223214762_Investigation_Report |  | 58546879-4ba3-5e22-99fb-6962eb489736 | MERGED | ORGANIZATION-8b9d6941 |
| LOCATION | b m complex |  | fact | 223214762_Investigation_Report | 61c8cdf9-ca09-4f15-8be6-384bfeab6fc6 |  | MERGED | LOCATION-0fbdc789 |
| PHONE | 8306895545 |  | fact | 223214762_Investigation_Report | ee0b7c21-585f-42be-af0d-9d176d19fda6 |  | MERGED | PHONE-a799785e |
| LOCATION | nana varachha surat | incident_site | field | 223214762_Investigation_Report |  | fb54b9d1-a063-50fb-8e1d-e7040e6a8561 | MERGED | LOCATION-78f8464f |
| LOCATION | moti nagar society |  | fact | 223214762_Investigation_Report | c9c7f929-07fa-40ad-af10-d64e0bf4c5e2 |  | MERGED | LOCATION-613a9380 |
| ORGANIZATION | navjivan hyundai garage |  | fact | 223214762_Investigation_Report | 38c5f96c-a0c1-416b-94d1-2ad17a6e4331 |  | MERGED | ORGANIZATION-02feaf6d |
| LOCATION | 394210:nr smc south |  | fact | 223214762_Investigation_Report | b11949ad-dd03-488f-bcca-664a054c2ab6 |  | MERGED | LOCATION-aad8d0cd |
| DATE | 2023-09-18 |  | fact | 223214762_Investigation_Report | 61b5db64-21d7-41c6-aa97-0560687fa96d |  | MERGED | DATE-8280dd7d |
| LOCATION | 395006: |  | fact | 223215102_Investigation_Report | bd8ebbd8-a1e3-40d6-8cb9-72d61ef6b176 |  | MERGED | LOCATION-4842a5c4 |
| LOCATION | nr smc south |  | fact | 223215102_Investigation_Report | 7beb767d-06d1-4aca-930a-d540467bfc64 |  | MERGED | LOCATION-a4d2e8fd |
| LOCATION | bamroli |  | fact | 223215102_Investigation_Report | dfa61523-9cc2-4a0f-b73f-48a07cbaff25 |  | MERGED | LOCATION-2743df9f |
| LOCATION | 394210: |  | fact | 223215102_Investigation_Report | dfa61523-9cc2-4a0f-b73f-48a07cbaff25 |  | MERGED | LOCATION-e32ca9e1 |
| PERSON | Vivekkumar M. Desai | surveyor | field | 223233211_Supplier_Bill |  | 40ef1e72-2fb3-586b-8dfa-a2438abf8ad0 | MERGED | PERSON-831fc87b |
| IDENTIFIER | sia73760 |  | fact | 223233211_Supplier_Bill | f9dbbd12-9850-43e6-8f32-22ea98a081ce |  | MERGED | IDENTIFIER-2326547a |
| DATE | 2024-10-03 |  | fact | 223233211_Supplier_Bill | a87848fc-f678-4980-b44d-df5414c1f945 |  | MERGED | DATE-f9dd01c4 |
| IDENTIFIER | lw06452 |  | fact | 223233211_Supplier_Bill | f13aa7f7-446d-47bf-bdc1-9338bc4a372d |  | MERGED | IDENTIFIER-df71eba3 |
| LOCATION | 395005:anand nagar society |  | fact | 223233211_Supplier_Bill | ca347980-9455-4d3e-8107-ee16948d9fb0 |  | MERGED | LOCATION-3f8aee7f |
| PHONE | 9879666447 |  | fact | 223233211_Supplier_Bill | 40b3d9c4-1061-46ff-9c3e-61be0afe3ae0 |  | MERGED | PHONE-dbc9c599 |
| EMAIL | desaivk29@gmail.com |  | fact | 223233211_Supplier_Bill | 308ed85a-9a3e-47ef-97cc-83644f93a01c |  | MERGED | EMAIL-167ce907 |
| IDENTIFIER | 6331 |  | fact | 223233211_Supplier_Bill | 9a386f04-27ec-445f-a39b-6af95f6cdc93 |  | MERGED | IDENTIFIER-6ef4bb32 |
| IDENTIFIER | 633128202334 |  | fact | 223233211_Supplier_Bill | f7830aef-0ab7-481b-9ae4-621914a76ed5 |  | MERGED | IDENTIFIER-8585a4b3 |
| LOCATION | 390007:4th floor atlantis |  | fact | 223233211_Supplier_Bill | 2de34a97-1d79-4205-9b52-0dfac6bc2838 |  | MERGED | LOCATION-2fbc3187 |
| IDENTIFIER | og242203180106005412 | policy | field | 223233211_Supplier_Bill |  | 156cf79d-43e2-5ba8-9dcd-f2a711c1731a | MERGED | IDENTIFIER-275477b1 |
| IDENTIFIER | oc242203180100002600 | claim | field | 223233211_Supplier_Bill |  | 25d236b9-bd17-5f7b-82af-1b5d293af92f | MERGED | IDENTIFIER-d213647e |
| IDENTIFIER | vdbagic0820236331 |  | fact | 223233211_Supplier_Bill | c46f93de-0b4e-43bc-adb8-a6c52e81ba7a |  | MERGED | IDENTIFIER-9b8fa648 |
| VEHICLE | HEON |  | fact | 223233211_Supplier_Bill | ad3ba200-5a2e-41d9-a4ed-142f39bb181f |  | MERGED | VEHICLE-f13be26e |
| AMOUNT | 96000 |  | fact | 223233211_Supplier_Bill | 9390c76a-577b-45e9-aa48-fe83fadd2d13 |  | NEW | AMOUNT-f96f1258 |
| DATE | 2023-08-06 |  | fact | 223233211_Supplier_Bill | 6a0d81ff-1826-45ac-a35e-72628d8b3ff0 |  | MERGED | DATE-c56ddedd |
| DATE | 2023-08-11 |  | fact | 223233211_Supplier_Bill | d8071691-5986-46bc-9269-1833087ddaf7 |  | MERGED | DATE-c9bfe25b |
| AMOUNT | 1500 |  | fact | 223233211_Supplier_Bill | eb54d727-2f84-4148-85fa-66777f86376c |  | NEW | AMOUNT-af8d88b4 |
| AMOUNT | 750 |  | fact | 223233211_Supplier_Bill | d1ce50fc-5384-444c-8bef-27076a8e0c75 |  | NEW | AMOUNT-c6d82f38 |
| AMOUNT | 2250 |  | fact | 223233211_Supplier_Bill | f93d7ffc-d1b2-463f-bd46-ccd9aa4135fe |  | NEW | AMOUNT-abcf2ceb |
| AMOUNT | 202 |  | fact | 223233211_Supplier_Bill | 25f887bb-f528-4d0c-8d91-4a532c0fd30d |  | NEW | AMOUNT-37a80287 |
| AMOUNT | 405 |  | fact | 223233211_Supplier_Bill | bba72994-23f7-4ecb-b00d-737f948aa85e |  | NEW | AMOUNT-72de4453 |
| AMOUNT | 2655 |  | fact | 223233211_Supplier_Bill | 0fa48cdc-35c5-414c-aad8-0704ea092e9a |  | NEW | AMOUNT-6fdd15ba |
| IDENTIFIER | 24ajapd2623k12n |  | fact | 223233211_Supplier_Bill | 2fdc1dcb-e44c-4e5d-984e-b9e73cda603e |  | MERGED | IDENTIFIER-8ac9c02c |
| IDENTIFIER | ajapd3623k |  | fact | 223233211_Supplier_Bill | d0d0d841-5aaa-4bf1-94af-122e26fbc3a6 |  | MERGED | IDENTIFIER-2a7ccad4 |
| IDENTIFIER | og242203180100006412 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 175f50b3-e731-413b-abb8-c4bcae86a601 |  | MERGED | IDENTIFIER-ee497ff2 |
| IDENTIFIER | 31871257 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | c214ab9a-03fc-4ff0-93c2-8fd71df617d3 |  | MERGED | IDENTIFIER-e8dfe0aa |
| DATE | 2023-08-12 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | e6143013-0dee-44e1-b2e6-ddd0b79f49f9 |  | MERGED | DATE-711daa5a |
| AMOUNT | 2440 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 15abe997-3d14-4697-ac05-2b27baf0cff2 |  | NEW | AMOUNT-e5a70bf3 |
| AMOUNT | 3660 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 15abe997-3d14-4697-ac05-2b27baf0cff2 |  | NEW | AMOUNT-93506f92 |
| AMOUNT | 730 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 6a502752-3aa8-4f37-959b-963cf22c2b54 |  | NEW | AMOUNT-23220b98 |
| AMOUNT | 292 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 6a502752-3aa8-4f37-959b-963cf22c2b54 |  | NEW | AMOUNT-388d4e03 |
| AMOUNT | 438 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 6a502752-3aa8-4f37-959b-963cf22c2b54 |  | NEW | AMOUNT-2f92daad |
| AMOUNT | 1208 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | cb12c40b-4c77-429c-9872-9ab621c23059 |  | NEW | AMOUNT-8d131b89 |
| AMOUNT | 483 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | cb12c40b-4c77-429c-9872-9ab621c23059 |  | NEW | AMOUNT-350f6b9b |
| AMOUNT | 725 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | cb12c40b-4c77-429c-9872-9ab621c23059 |  | NEW | AMOUNT-01fd8fae |
| AMOUNT | 608 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | ecfe5dae-9639-4ed8-b294-8bc37e3fb6ea |  | NEW | AMOUNT-bbcda0b5 |
| AMOUNT | 243 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | ecfe5dae-9639-4ed8-b294-8bc37e3fb6ea |  | NEW | AMOUNT-2ca23d4f |
| AMOUNT | 365 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | ecfe5dae-9639-4ed8-b294-8bc37e3fb6ea |  | NEW | AMOUNT-b2855118 |
| AMOUNT | 879 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | a05b6853-99ba-4220-8ca8-8057a7be79b2 |  | NEW | AMOUNT-918d1c96 |
| AMOUNT | 352 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | a05b6853-99ba-4220-8ca8-8057a7be79b2 |  | NEW | AMOUNT-ebbacf28 |
| AMOUNT | 527 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | a05b6853-99ba-4220-8ca8-8057a7be79b2 |  | NEW | AMOUNT-d6ef577d |
| AMOUNT | 5027 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 045a9379-8c46-4671-b277-f27cbe02257e |  | NEW | AMOUNT-e18744dc |
| AMOUNT | 2011 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 045a9379-8c46-4671-b277-f27cbe02257e |  | NEW | AMOUNT-1629ec25 |
| AMOUNT | 3016 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 045a9379-8c46-4671-b277-f27cbe02257e |  | NEW | AMOUNT-99466d70 |
| AMOUNT | 3036 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 9f16565f-8f4e-402f-a254-a558bba304c2 |  | NEW | AMOUNT-48d3e415 |
| AMOUNT | 1214 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 9f16565f-8f4e-402f-a254-a558bba304c2 |  | NEW | AMOUNT-c916323a |
| AMOUNT | 1822 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 9f16565f-8f4e-402f-a254-a558bba304c2 |  | NEW | AMOUNT-850ab8eb |
| AMOUNT | 2945 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | a25e85fc-2b73-4e3b-8444-b60de7322c4c |  | NEW | AMOUNT-4277943d |
| AMOUNT | 1178 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | a25e85fc-2b73-4e3b-8444-b60de7322c4c |  | NEW | AMOUNT-c6ef968f |
| AMOUNT | 1767 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | a25e85fc-2b73-4e3b-8444-b60de7322c4c |  | NEW | AMOUNT-dc5427ea |
| AMOUNT | 4266 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | f4bcab32-d5ff-4223-b209-12eb169a8b1a |  | NEW | AMOUNT-06c8c6ce |
| AMOUNT | 6400 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | f4bcab32-d5ff-4223-b209-12eb169a8b1a |  | NEW | AMOUNT-71351f07 |
| AMOUNT | 512 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | d830b019-6839-473b-8db5-a077d74ac974 |  | NEW | AMOUNT-fda5a8b0 |
| AMOUNT | 588 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | f138cc31-f3be-48d6-bbff-3686b174a079 |  | NEW | AMOUNT-c72bac89 |
| AMOUNT | 294 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | f138cc31-f3be-48d6-bbff-3686b174a079 |  | NEW | AMOUNT-00925b76 |
| AMOUNT | 1301 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 15ca73ad-496a-4cc2-b9b6-03f46109008b |  | NEW | AMOUNT-bea80f13 |
| AMOUNT | 347 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 87b9b495-6bd4-413f-8351-5094f13964b4 |  | NEW | AMOUNT-53ea3d52 |
| AMOUNT | 173 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 87b9b495-6bd4-413f-8351-5094f13964b4 |  | NEW | AMOUNT-20b70cd9 |
| AMOUNT | 3061 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 3700bb77-3989-48b5-9aed-40dc414f39f3 |  | NEW | AMOUNT-9a6cdaf6 |
| AMOUNT | 1530 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 3700bb77-3989-48b5-9aed-40dc414f39f3 |  | NEW | AMOUNT-22139de6 |
| AMOUNT | 127 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | d1e9b07e-7631-4c94-9bf6-c416f5b50900 |  | NEW | AMOUNT-fa4574c5 |
| AMOUNT | 64 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | d1e9b07e-7631-4c94-9bf6-c416f5b50900 |  | NEW | AMOUNT-779dbddc |
| AMOUNT | 1605 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | f20300ac-1de0-4c9a-935b-e370ad812c75 |  | NEW | AMOUNT-9145892f |
| AMOUNT | 802 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | f20300ac-1de0-4c9a-935b-e370ad812c75 |  | NEW | AMOUNT-1e91d4bd |
| AMOUNT | 461 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 0e676789-4b57-4f8b-b53e-5e0b7907e4b5 |  | NEW | AMOUNT-c9865e77 |
| AMOUNT | 230 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 0e676789-4b57-4f8b-b53e-5e0b7907e4b5 |  | NEW | AMOUNT-5582d06c |
| AMOUNT | 32537 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 148228ff-c0f0-409a-83d3-09f595b9ec02 |  | NEW | AMOUNT-36548950 |
| AMOUNT | 13015 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 148228ff-c0f0-409a-83d3-09f595b9ec02 |  | NEW | AMOUNT-0717d841 |
| AMOUNT | 19622 |  | fact | 223233267_Signed_Licensed_Surveyor_Report | 148228ff-c0f0-409a-83d3-09f595b9ec02 |  | NEW | AMOUNT-46a185ce |
| IDENTIFIER | oc24220318010006512 | policy | field | 223237590_Signed_Licensed_Surveyor_Report |  | 9c07b425-0de6-5ca8-b3d5-5cc63bccb8aa | MERGED | IDENTIFIER-18fb2ec0 |
| IDENTIFIER | g31adm199755 | engine | field | 223237590_Signed_Licensed_Surveyor_Report |  | 955daabe-5799-5646-9365-5d6af91640f6 | MERGED | IDENTIFIER-712f8fbd |
| VEHICLE | 2013 |  | fact | 223237590_Signed_Licensed_Surveyor_Report | 8762fadb-3a30-4971-ad35-168243b73b02 |  | MERGED | VEHICLE-29702fbd |
| VEHICLE | METALLIC |  | fact | 223237590_Signed_Licensed_Surveyor_Report | 3ea2e20a-78ae-44bf-ad6b-17642cad71f9 |  | MERGED | VEHICLE-f72caf3a |
| VEHICLE | PRIVATECAR |  | fact | 223237590_Signed_Licensed_Surveyor_Report | 2a641d7b-69e4-40f2-9a8a-1225be705e37 |  | MERGED | VEHICLE-20073772 |
| VEHICLE | 123 |  | fact | 223237590_Signed_Licensed_Surveyor_Report | de062537-7987-497d-a096-324fb693555e |  | MERGED | VEHICLE-282ea85c |
| IDENTIFIER | guj0510281370 | driving_licence | field | 223237590_Signed_Licensed_Surveyor_Report |  | 94341b74-9c5d-5d98-b8b6-18a1ddcfcd89 | NEW | IDENTIFIER-50e9a305 |
| DATE | 2008-04-15 |  | fact | 223237590_Signed_Licensed_Surveyor_Report | 84a05ab3-8612-4613-82cc-79d704b6b886 |  | MERGED | DATE-f82810c7 |
| AMOUNT | 29369 |  | fact | 223237590_Signed_Licensed_Surveyor_Report | bbd42c13-d3b7-4cb8-a95e-36c399616981 |  | NEW | AMOUNT-fd951108 |
| AMOUNT | 49573 |  | fact | 223237590_Signed_Licensed_Surveyor_Report | d8e588e3-e00e-40db-bc8b-370c97cb5d83 |  | NEW | AMOUNT-82a2bdbc |
| AMOUNT | 21462 |  | fact | 223237590_Signed_Licensed_Surveyor_Report | e0d9d549-a4a8-4a64-b0bb-17cf726856d4 |  | NEW | AMOUNT-f83f8ddf |
| AMOUNT | 77942 |  | fact | 223237590_Signed_Licensed_Surveyor_Report | 3637db6e-4e07-4b28-823f-a5a45144a4b7 |  | NEW | AMOUNT-5c5eef07 |
| PERSON | U.M.Desai | surveyor | field | 223237590_Signed_Licensed_Surveyor_Report |  | cd318f6a-29bb-5f64-bd6b-ae41332ab0e5 | MERGED | PERSON-d74f92c8 |
| IDENTIFIER | oc2422181801005412 | claim | field | 223404609_Follow-up_Letters |  | 3ac8420d-a7b6-5b2e-a983-73ddc795edd7 | NEW | IDENTIFIER-f18b6171 |
| IDENTIFIER | oc2l320718012660 | policy | field | 223404609_Follow-up_Letters |  | 8ed26826-f591-5c2b-9991-502a43e8ad4e | NEW | IDENTIFIER-ee0bda1f |
| EMAIL | bagshelp@bajajallianz.co.in |  | fact | 223404609_Follow-up_Letters | 6cf4b42a-7db1-458e-aa1b-5a762e86fabc |  | MERGED | EMAIL-cedb4048 |
| ORGANIZATION | www bajajallianz com |  | fact | 223404609_Follow-up_Letters | 86e7132a-090b-4052-b063-792ad736f206 |  | MERGED | ORGANIZATION-a07e08c8 |
| LOCATION | 411006:bajaj allianz navi |  | fact | 223404609_Follow-up_Letters | 19ef15cc-9c87-47df-8b00-d9a09ac8abb1 |  | NEW | LOCATION-a07104bc |
| ORGANIZATION | rda |  | fact | 223404609_Follow-up_Letters | a61a66e3-5d7c-4e11-901f-f6d8bb24c350 |  | NEW | ORGANIZATION-4571df0e |
| VEHICLE | UNKNOWN |  | fact | 223404609_Follow-up_Letters | e22275f9-c982-4d45-9e48-1023ddfb6727 |  | NEW | VEHICLE-ac93e1ab |
| DATE | 7 |  | fact | 223404609_Follow-up_Letters | ef75e9f5-2cf0-4e10-a255-cdbf37a3ea8e |  | NEW | DATE-917264f4 |
| IDENTIFIER | rg289062596in |  | fact | 223404609_Follow-up_Letters | 24839594-bdcd-451d-acfa-982f551a6c6a |  | MERGED | IDENTIFIER-bdfb1fea |
| IDENTIFIER | u66010pn2000plc015329 |  | fact | 223404609_Follow-up_Letters | 87f7966c-0a0b-459c-8562-0c4cd92246bc |  | MERGED | IDENTIFIER-6f94dbaa |
| DATE | 2023-09-21 |  | fact | 223721550_Follow-up_Letters | d58fb330-d8b5-418e-9317-b8bd8d54f1f8 |  | MERGED | DATE-a2b5e864 |
| PHONE | 9537436355 |  | field | 223721550_Follow-up_Letters |  | 436f15e1-88eb-59a3-9fa9-5decda2fa709 | MERGED | PHONE-c230d4c0 |
| PERSON | Bipin Shiroya | signatory | field | 223721550_Follow-up_Letters |  | f993cf8f-5397-50d9-93e9-20778721f077 | MERGED | PERSON-e273dca7 |
| PHONE | 2653960861 |  | fact | 223721550_Follow-up_Letters | 4e50a004-62df-4f27-b2fd-4534d678d992 |  | MERGED | PHONE-09d714d6 |
| PHONE | 9898994381 |  | fact | 223721550_Follow-up_Letters | 44047999-9711-4acb-83de-988eb4cb6a97 |  | MERGED | PHONE-538a62e9 |
| IDENTIFIER | 113 |  | fact | 223721550_Follow-up_Letters | 0d31f11b-ed81-48e4-a553-0ecf92aee299 |  | MERGED | IDENTIFIER-34f0e517 |
| LOCATION | 390007:bajaj allianz general |  | fact | 223721550_Follow-up_Letters | 81331896-b7a6-4576-85b9-caaae2cac0a6 |  | MERGED | LOCATION-b19c8d4e |
| PHONE | 7507245858 |  | fact | 223721550_Follow-up_Letters | 5eba6e7c-06fd-4c54-9c16-65b2ee631cf7 |  | MERGED | PHONE-e3d8a00f |
| PHONE | 8308943060 |  | fact | 223721550_Follow-up_Letters | 03e0475c-9f16-425d-b364-59711da85521 |  | MERGED | PHONE-49d1aa90 |
| PHONE | 18002095858 |  | fact | 223721550_Follow-up_Letters | fc05e994-a4c8-4617-abf9-c40595d73316 |  | MERGED | PHONE-21f3947b |
| GENERIC_IDENTIFIER | gj27ak0736 | vehicle_registration | field | 218890832_Registration_Certificate |  | cb053bad-36eb-5b9e-a1ca-cea5d70d2c8d | MERGED | GENERIC_IDENTIFIER-50541997 |
| GENERIC_IDENTIFIER | gj230808v2160368 | application_number_for_registration | field | 218890832_Registration_Certificate |  | 526778ec-b1fd-54bc-838d-aef5144ac7fe | MERGED | GENERIC_IDENTIFIER-dbbdac9f |
| GENERIC_IDENTIFIER | gj230808c9783109 | receipt_number | field | 218890832_Registration_Certificate |  | 20d50f0d-6952-54ee-af07-8278a0bd8db7 | MERGED | GENERIC_IDENTIFIER-173b8426 |
| GENERIC_IDENTIFIER | 20634 | amount_2 | field | 218890832_Registration_Certificate |  | 769f23ec-9df5-56ba-a28c-7c5c7fd925ac | MERGED | GENERIC_IDENTIFIER-2cf5bf93 |
| PERSON | Bajaj Finance Limited |  | field | 218890832_Registration_Certificate |  | cdbed2f8-efde-549e-b0e7-c19b51cabbf0 | MERGED | PERSON-68db358c |
| IDENTIFIER | handwritten21022029 | chassis | field | 218890910_Claim_Form |  | 81d95289-ce1e-5aa7-bc00-f115e1600f07 | NEW | IDENTIFIER-04247927 |
| PHONE | 20245 |  | field | 218890910_Claim_Form |  | 28261d56-f1f1-5042-a297-bd02b0a3eab2 | NEW | PHONE-70e0866e |
| IDENTIFIER | handwrittenujosio02hadi061 | driving_licence | field | 218890910_Claim_Form |  | c19564fc-51aa-563b-9525-5b838a24f812 | NEW | IDENTIFIER-cbb8244d |
| PERSON | [Handwritten: Dram E3 H Hdyar] | insured | field | 218890910_Claim_Form |  | be7dbba9-b9da-5f65-b521-63dc7dca1bdd | NEW | PERSON-64c744f1 |
| PERSON | [Handwritten: Fir Hadi H Hdyar Ishahdi] | driver | field | 218890910_Claim_Form |  | 41b2536e-723c-5262-aa53-9b1967335651 | NEW | PERSON-3597ef81 |
| PERSON | [Handwritten: Maha 3 Hdyar] |  | field | 218890910_Claim_Form |  | 425914a8-7792-5126-a99d-ec03bf364f94 | NEW | PERSON-61e3d612 |
| LOCATION | handwritten nema vasselley | incident_site | field | 218890910_Claim_Form |  | 6a0d3ddc-3b6f-59b3-a578-248116d49115 | NEW | LOCATION-cd39ec28 |
| GENERIC_IDENTIFIER | 20250410 | date | field | 218890910_Claim_Form |  | c8bd3410-27c4-5697-ab31-930e56095b9c | NEW | GENERIC_IDENTIFIER-f458460b |
| GENERIC_IDENTIFIER | 20230809 | document_date | field | 218890965_Repair_Estimate |  | 5dec1c3c-3916-5727-966d-8f059a56d791 | MERGED | GENERIC_IDENTIFIER-6bb1b106 |
| GENERIC_IDENTIFIER | irdan113rp00251v01200102 | uin | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | GENERIC_IDENTIFIER-71397b81 |
| GENERIC_IDENTIFIER | 20230802 | policy_issued_on | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | GENERIC_IDENTIFIER-a4ef8de7 |
| GENERIC_IDENTIFIER | 399252385 | customer_id | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | GENERIC_IDENTIFIER-644bfd02 |
| GENERIC_IDENTIFIER | 24aabcb5730g1z3 | gstin, gstin_2 | field | 218891028_Policy_Copy |  | 37945fed-5adb-5b19-9881-6f69d0e08cb4 | MERGED | GENERIC_IDENTIFIER-bdc981a1 |
| PERSON | 24 - Gujarat |  | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | PERSON-d2e68da0 |
| GENERIC_IDENTIFIER | 5883382461 | invoice_no | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | GENERIC_IDENTIFIER-f8a00fa9 |
| GENERIC_IDENTIFIER | aabcb5730g | company_pan_no | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | GENERIC_IDENTIFIER-d434e364 |
| IDENTIFIER | 0 | policy | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | IDENTIFIER-5bcc5639 |
| GENERIC_IDENTIFIER | 20240802 | expiry_on | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | GENERIC_IDENTIFIER-9a5c413e |
| GENERIC_IDENTIFIER | 02612256882 | contact_no | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | GENERIC_IDENTIFIER-ff8a6e85 |
| GENERIC_IDENTIFIER | gj27ahmedabad | name_of_the_registration_authority | field | 218891028_Policy_Copy |  | 21560b49-debb-5c2d-b869-04129a63d7f4 | MERGED | GENERIC_IDENTIFIER-ef21fec9 |
| GENERIC_IDENTIFIER | botpv1228n | pan_card_number | field | 219032034_AML_Documents |  | b4790284-da4f-5720-a039-71157369460f | MERGED | GENERIC_IDENTIFIER-c0dd6c21 |
| ORGANIZATION | income tax department government of india | issuing_authority | field | 219032034_AML_Documents |  | b4790284-da4f-5720-a039-71157369460f | MERGED | ORGANIZATION-4d41977d |
| GENERIC_IDENTIFIER | 09082023 | date_of_gate_pass_issuance | field | 219032145_Job_Card |  | cb95a01a-9cae-5d0c-ae14-d615bdb7c30d | MERGED | GENERIC_IDENTIFIER-0ccba303 |
| GENERIC_IDENTIFIER | gh27aa0136 | vehicle_registration | field | 219032145_Job_Card |  | 465d5717-b929-5a90-a4a8-47945b1b586e | MERGED | GENERIC_IDENTIFIER-3ea4698a |
| GENERIC_IDENTIFIER | 219213 | odometer_reading_in_kilometers_at_time_o | field | 219032145_Job_Card |  | 6c6911be-b180-5dbb-8e88-c874cb836b6f | MERGED | GENERIC_IDENTIFIER-149b0478 |
| GENERIC_IDENTIFIER | et23080090 | repair_estimate_number | field | 219358654_Repair_Estimate |  | e71dc912-d4d4-5208-bd52-026e499babd1 | MERGED | GENERIC_IDENTIFIER-446682bf |
| GENERIC_IDENTIFIER | gj27aa0736 | vehicle_registration | field | 219358654_Repair_Estimate |  | b50c1b67-d7bc-5b78-91ac-71a40ec1ea4c | MERGED | GENERIC_IDENTIFIER-e0e70136 |
| WORKSHOP | navjivan motors |  | field | 219358654_Repair_Estimate |  | fcde1f08-f462-5b6b-ae41-91fb4411d169 | MERGED | WORKSHOP-8d096a69 |
| GENERIC_IDENTIFIER | 20131017 | issue_date | field | 219430367_Pre_Inspection_Photographs_Reports |  | 6d457fdb-2df6-5f55-acf0-ec71b78510db | MERGED | GENERIC_IDENTIFIER-8673a353 |
| GENERIC_IDENTIFIER | 20281016 | expiry_date | field | 219430367_Pre_Inspection_Photographs_Reports |  | 5f42d811-82b3-549d-98b2-387d5cbb1f8a | MERGED | GENERIC_IDENTIFIER-2c9d791a |
| GENERIC_IDENTIFIER | 20230919 | statement_date | field | 222633146_Statement_of_Insured |  | d7a4eeb6-3459-5c6f-9d1e-b5261140dd24 | MERGED | GENERIC_IDENTIFIER-9f33a866 |
| PHONE | 9411411 |  | field | 222633146_Statement_of_Insured |  | e36f046f-8e44-55f2-855b-a6820d59eafb | NEW | PHONE-0db27d7c |
| PERSON | [Gujarati Text - Name Not Clearly Legible] | driver | field | 222633187_Statement_of_Driver |  | 5f0e9b00-4075-5536-836b-ee175adbf2d0 | NEW | PERSON-401bb356 |
| ORGANIZATION | hyundai i10 |  | field | 222633313_Vehicle_Damage_Photo |  | 4b25eb38-fec7-59f7-b330-e18d1289339d | MERGED | ORGANIZATION-c3ae037d |
| GENERIC_IDENTIFIER | 9227463964 | vehicle_registration | field | 222633435_Any_Other |  | 483da377-4754-5d23-a214-6de83e085427 | MERGED | GENERIC_IDENTIFIER-b91c30a8 |
| GENERIC_IDENTIFIER | 27072023 | date_on_vehicle_purchase_form | field | 222633435_Any_Other |  | 258bbbc1-3e42-5dae-9a6f-9388da182ebb | MERGED | GENERIC_IDENTIFIER-41e08dd5 |
| GENERIC_IDENTIFIER | 9455504 | vehicle_registration_2 | field | 222633435_Any_Other |  | f7aa5b21-44a6-5c5f-b03b-73b0574b2c16 | NEW | GENERIC_IDENTIFIER-e34772fb |
| GENERIC_IDENTIFIER | 1510664 | amount | field | 222633435_Any_Other |  | 79e869fa-a369-5f53-99a6-4775834adf97 | MERGED | GENERIC_IDENTIFIER-5d6138f2 |
| GENERIC_IDENTIFIER | 29950 | amount_2 | field | 222633435_Any_Other |  | 8e529827-09bd-5efe-827e-907c46a0740c | NEW | GENERIC_IDENTIFIER-18c292da |
| GENERIC_IDENTIFIER | 1510652 | amount_3 | field | 222633435_Any_Other |  | e06f85a7-8c5d-5a73-b79c-a4d40754d09a | MERGED | GENERIC_IDENTIFIER-96d8055e |
| GENERIC_IDENTIFIER | 50001201 | odometer_reading | field | 222633435_Any_Other |  | a82e6ac2-5f51-5127-8269-c6e97eceb9d7 | NEW | GENERIC_IDENTIFIER-fc5133a2 |
| GENERIC_IDENTIFIER | 149000 | amount_4 | field | 222633435_Any_Other |  | 50b2ea3f-6af7-5258-9e09-2ba1e337e573 | NEW | GENERIC_IDENTIFIER-420dfb37 |
| PERSON | [Handwritten: Illegible - Appears To Be Insured'S Name] | insured | field | 222696526_Statement_of_Insured |  | 3d485a9a-2210-5c14-a899-fe2fa583fe27 | NEW | PERSON-7292bfbb |
| IDENTIFIER | BOTPV1128N | pan | field | 223214762_Investigation_Report |  | d30dd126-4aab-5cf4-8656-fa303d616671 | MERGED | IDENTIFIER-335b41dd |
| GENERIC_IDENTIFIER | 8306895545 | phone_number_2 | field | 223214762_Investigation_Report |  | ddf770a6-d76d-5b18-826d-46f8d25fd3cc | MERGED | GENERIC_IDENTIFIER-430c0b7e |
| GENERIC_IDENTIFIER | 395006 | pin_code_of_insured's_address | field | 223214762_Investigation_Report |  | d82d4e43-efcf-5bbf-8331-d0a9200450df | MERGED | GENERIC_IDENTIFIER-4c33da7e |
| GENERIC_IDENTIFIER | 394210 | pin_code_of_garage_address | field | 223214762_Investigation_Report |  | 668d4e57-70a1-539a-b177-3ee719fa8d35 | MERGED | GENERIC_IDENTIFIER-e6f4960f |
| WORKSHOP | navjivan hyundai garage |  | field | 223214762_Investigation_Report |  | 8d31b582-b293-5687-925a-9a0d9c86d743 | MERGED | WORKSHOP-b501c66f |
| PERSON | Abhishek Gaur |  | field | 223214762_Investigation_Report |  | 33dc536e-adc6-5f4a-b532-f6299ef140cd | NEW | PERSON-dce11559 |
| GENERIC_IDENTIFIER | 20230918 | report_date, date | field | 223214762_Investigation_Report |  | e0a0e9bc-5da6-5426-bafd-cddc16de9526 | MERGED | GENERIC_IDENTIFIER-4f530df5 |
| GENERIC_IDENTIFIER | 633128202334 | reference_number_for_the_bill | field | 223233211_Supplier_Bill |  | 87863a07-7d79-584e-977c-374aa5c271f6 | MERGED | GENERIC_IDENTIFIER-26459e28 |
| GENERIC_IDENTIFIER | 96000 | amount | field | 223233211_Supplier_Bill |  | de074bf4-bb78-5fcb-833d-c200721b81a1 | MERGED | GENERIC_IDENTIFIER-3ec29741 |
| GENERIC_IDENTIFIER | 24ajapd2623k12n | gstin | field | 223233211_Supplier_Bill |  | b4e48232-8a37-503b-9543-22a263acbfb0 | MERGED | GENERIC_IDENTIFIER-f01ec92f |
| IDENTIFIER | AJAPD3623K | pan | field | 223233211_Supplier_Bill |  | 2370200f-39d0-5d7f-86ac-dc77bcebf2db | MERGED | IDENTIFIER-789a5b3b |
| GENERIC_IDENTIFIER | 20230806 | date_2 | field | 223233211_Supplier_Bill |  | f5a7455e-43c6-563e-bb94-da5639973546 | MERGED | GENERIC_IDENTIFIER-4a0a5fda |
| GENERIC_IDENTIFIER | 20230811 | date_3 | field | 223233211_Supplier_Bill |  | 0945dca5-8fe0-5f8b-bb0d-0c90cd159e29 | MERGED | GENERIC_IDENTIFIER-1f2206f4 |
| GENERIC_IDENTIFIER | 31871257 | claim_id_for_parts_report | field | 223237590_Signed_Licensed_Surveyor_Report |  | e3d55aeb-f74b-57e4-af4c-5b37dc4e8b98 | MERGED | GENERIC_IDENTIFIER-3d77b285 |
| GENERIC_IDENTIFIER | 77942 | amount | field | 223237590_Signed_Licensed_Surveyor_Report |  | b5b0694a-fe11-5375-a7e3-9ea1c95c80f3 | MERGED | GENERIC_IDENTIFIER-ea0b9f01 |
| GENERIC_IDENTIFIER | 29369 | amount_2 | field | 223237590_Signed_Licensed_Surveyor_Report |  | 5adc1af0-8659-5a24-9158-9eced5059d6d | MERGED | GENERIC_IDENTIFIER-defa0085 |
| GENERIC_IDENTIFIER | 49573 | amount_3 | field | 223237590_Signed_Licensed_Surveyor_Report |  | 1d747cbf-145a-582e-8a9b-fd24e3e37415 | MERGED | GENERIC_IDENTIFIER-d7076254 |
| GENERIC_IDENTIFIER | 21462 | amount_5 | field | 223237590_Signed_Licensed_Surveyor_Report |  | acc916f4-6a09-5049-a8c6-91f00f016ca7 | NEW | GENERIC_IDENTIFIER-9a1423fb |
| GENERIC_IDENTIFIER | 03aug2023 | date | field | 223237590_Signed_Licensed_Surveyor_Report |  | 17a93e4b-857c-5d00-afa1-9019522d3c40 | MERGED | GENERIC_IDENTIFIER-7b58bbfd |
| GENERIC_IDENTIFIER | 02aug2024 | expiry_date | field | 223237590_Signed_Licensed_Surveyor_Report |  | d9c30ebd-9db8-5960-8cdd-c7858b4077fe | MERGED | GENERIC_IDENTIFIER-3c6b5b2f |
| GENERIC_IDENTIFIER | 08aug2023 | date_2 | field | 223237590_Signed_Licensed_Surveyor_Report |  | 9127bdf1-9bf6-5593-95ef-b39d8bc439d8 | MERGED | GENERIC_IDENTIFIER-8cf58cea |
| GENERIC_IDENTIFIER | 10aug2023 | date_3 | field | 223237590_Signed_Licensed_Surveyor_Report |  | e3f43238-204a-5ab5-bb5e-a0e84bf065aa | MERGED | GENERIC_IDENTIFIER-eaf2f861 |
| GENERIC_IDENTIFIER | 12aug2023 | date_4 | field | 223237590_Signed_Licensed_Surveyor_Report |  | e2a8df6a-fb79-5669-a802-ffb732357e30 | MERGED | GENERIC_IDENTIFIER-5895e4db |
| GENERIC_IDENTIFIER | 17oct2013 | date_5 | field | 223237590_Signed_Licensed_Surveyor_Report |  | c02a37d8-80bc-59c7-8a0e-83468bdfcfb7 | NEW | GENERIC_IDENTIFIER-fcc5d0a2 |
| GENERIC_IDENTIFIER | 15apr2008 | issue_date | field | 223237590_Signed_Licensed_Surveyor_Report |  | 4e4cc9e0-a87a-5728-9602-ebb13dea86ae | NEW | GENERIC_IDENTIFIER-124af453 |
| GENERIC_IDENTIFIER | 11apr2026 | expiry_date_2 | field | 223237590_Signed_Licensed_Surveyor_Report |  | ebd98e06-afc4-5c5b-aff9-7890234ce307 | NEW | GENERIC_IDENTIFIER-1c5b0484 |
| GENERIC_IDENTIFIER | u66010pn2000plc015329 | corporate_identification_number_of_bajaj, corporate_identification_number_(cin) | field | 223404609_Follow-up_Letters |  | 3ac7b9f2-31d4-5fd8-8514-0c5943d046a5 | MERGED | GENERIC_IDENTIFIER-047eaf8f |
| GENERIC_IDENTIFIER | rg289062596in | barcode_number_on_document | field | 223404609_Follow-up_Letters |  | 9716903f-e9a8-5ddd-b1ad-0965d04ae9bd | NEW | GENERIC_IDENTIFIER-2e4419dd |
| LOCATION | vadodara |  | field | 223404609_Follow-up_Letters |  | dcf67340-9f34-5219-bd2d-c12a7573d3ad | MERGED | LOCATION-a58c8141 |
| GENERIC_IDENTIFIER | 20230818 | date | field | 223404609_Follow-up_Letters |  | 7e279ee9-ec1a-5988-a3b9-feec8a4e9834 | MERGED | GENERIC_IDENTIFIER-06538773 |
| GENERIC_IDENTIFIER | 02653960861 | phone_number_2 | field | 223721550_Follow-up_Letters |  | 10c5d622-adbc-5001-9ebd-fc2645434e62 | MERGED | GENERIC_IDENTIFIER-1bbabde3 |
| GENERIC_IDENTIFIER | 7507245858 | phone_number_4 | field | 223721550_Follow-up_Letters |  | e3c56b84-1c19-5347-b584-c03300c68ed1 | MERGED | GENERIC_IDENTIFIER-a811bede |
| GENERIC_IDENTIFIER | 8308943060 | phone_number_5 | field | 223721550_Follow-up_Letters |  | bcb1c49e-d3ad-52e6-b3b9-d5b8c7b0ac2a | MERGED | GENERIC_IDENTIFIER-64da2111 |
| GENERIC_IDENTIFIER | 18002095858 | phone_number_6 | field | 223721550_Follow-up_Letters |  | 18c8d7dc-a3cb-5861-908a-1df1bd2a2983 | MERGED | GENERIC_IDENTIFIER-1c66676f |
| VEHICLE | 113 |  | field | 223721550_Follow-up_Letters |  | 7f71b964-2429-51ec-b964-bdad4803384d | MERGED | VEHICLE-205e6e1d |
| LOCATION | surat city surat |  | field | 223721550_Follow-up_Letters |  | 3629fc10-2c04-5e9f-87b9-b96bae2e1d21 | MERGED | LOCATION-6385d0f5 |
| LOCATION | vadodara gujarat |  | field | 223721550_Follow-up_Letters |  | 4d13cbab-4b27-5ce7-abe5-7690a79d4ac9 | MERGED | LOCATION-d7275ed0 |

### H.2 — Resolution trace

**Deterministic name pre-pass — PERSON variants collapsed:**

| variant_value | canonical_value |
| --- | --- |
| Maheshkumar Indrasing Vasava | Maheshwaram Indrasingh Vasava |
| Prakash Chaudhari | Prakashbhai Chaudhari |
| Prakashbhai Chaudary | Prakashbhai Chaudhari |
| Mahesh Vasava | Maheshkumar Vasava |


_LLM soft-match: no aliases applied this run (either the LLM returned no matches, or none survived the membership + type safety guards in `_apply_llm_resolutions`)._

LLM resolution candidates evaluated: 21

### H.3 — Neo4j relationships

_Cypher counts for the current claim node are queried by the persistence-audit section (K)._

## I — Embeddings

Qdrant collection: `sqc_document_chunks`
Total chunks for this claim: **79**

| qdrant_point_id | chunk_index | source_document_id | doc_type | embedding_source | embedding_model | preview |
| --- | --- | --- | --- | --- | --- | --- |
| 041f405b-c8fc-4127-b2da-8a8f6d13965a | 8 | 223214762_Investigation_Report | correspondence | text |  | so he informed his friend Prakshbhai Chaudhari who works with him to drive the IV whenever required. On 08-08-2023 at around 21:15 when they were going to fill up fuel in the IV and as per the insure… |
| 047969c2-f632-421a-9bee-e01548caaf68 | 6 | 223215102_Investigation_Report | correspondence | text |  | rict SURAT \| State GUJARAT \| Pin 0 \| Contact No 0 Version of Eye witness No eyewitness is available. Driver Details Personal meeting with driver Yes \| Reason [blank] Whether Address of driver vis… |
| 0fb0bb26-655c-4a9a-b560-c6b71bf52ebc | 1 | 222633313_Vehicle_Damage_Photo | photograph | text |  | cle. Red tail lights visible. Vehicle parked in lot with other vehicles and buildings in background. Page 5: Overhead/angled view showing front-end damage more clearly. Hood is significantly crushed.… |
| 135332e8-205f-4155-851f-adf53308cbf6 | 8 | 223215102_Investigation_Report | correspondence | text |  | so he informed his friend Prakshbhai Chaudhari who works with him to drive the IV whenever required. On 08-08-2023 at around 21:15 when they were going to fill up fuel in the IV and as per the insure… |
| 151141a8-2a08-4c07-98f6-5b3e99c97c39 | 2 | 223404609_Follow-up_Letters | correspondence | text |  | : Bajaj Allianz General Insurance Co. Ltd., 4th Floor, Atlantis Heritage, B/H Atlantis Heights, Opp. Swagat Petrol Pump, Sarabhai Main Road, Vadodara - 390007 For more details, please visit: https://… |
| 18326c98-d2e5-442b-96d1-dbb4f5e7f504 | 4 | 223237590_Signed_Licensed_Surveyor_Report | accident_report | text |  | red don't have MDL to driver car \| \| \|  [HANDWRITTEN SIGNATURE: U.M.Desai] Surveyor Signature  Auth. BAGIC Signature  Report Issued without prejudice subject to policy terms and conditions. |
| 1838827f-3ea2-4430-8aa7-a1f87d641335 | 2 | 222633313_Vehicle_Damage_Photo | photograph | text |  | ng. Headlights damaged. Front bumper area affected. Vehicle registration GJ27AA0736 clearly visible. Parked in lot with wall and other vehicles visible. |
| 1a25365a-946e-40aa-b984-437fd4ff1454 | 1 | 223233211_Supplier_Bill | repair_estimate | text |  | F SUPPLY: GUJARAT DATE OF LOSS: 6-Aug-2023 DATE OF SURVEY: 11-Aug-2023 STATE OF SUPPLY: GUJARAT  01. PROFESSIONAL FEES: SPOT SURVEY FINAL SURVEY RE-INSPECTION  RATE: AMOUNT: Rs. 1,500.00 Rs. 1,500.00… |
| 1f4b50a0-412f-44d2-a03a-3873dcf04978 | 0 | 223404609_Follow-up_Letters | correspondence | text |  | Bajaj Allianz General Insurance Co. Ltd. 4th Floor, Atlantis Heritage, B/H Atlantis Heights, Opp. Swagat Petrol Pump, Sarabhai Main Road, Vadodara - 390007. OC-2L-3207-1801-2660  [BARCODE: RG28906259… |
| 21b659aa-d6d0-4e09-85a0-054c6ca935c7 | 1 | 223404609_Follow-up_Letters | correspondence | text |  | nce to above reported claim as per documents submitted by your good self and report of RDA approved. As per documents submitted by your good self and report of RDA approved, it is established that th… |
| 222d3f73-7ac6-431a-8458-2e322d2c790d | 2 | 223214762_Investigation_Report | correspondence | text |  | On 08-08-2023 after dinner, he and his friend Prakash Chaudhari were going to fill petrol in the IV. When they were passing Nana Varachha in front of Motinagar a motorcycle came from the wrong side s… |
| 250c3564-4de1-4ecd-aec2-05fe19ef169b | 1 | 223721550_Follow-up_Letters | correspondence | text |  | with proper documentary evidences till date as per the requirement for further review of your claim. In view of above your claim stands repudiated as per policy terms & conditions. "Please note that … |
| 255564e1-e71e-481f-adb6-0c7698ed8eb0 | 5 | 223215102_Investigation_Report | correspondence | text |  | ges in correlation with Injuries and Manner of accident The IV has been damaged from the front side. Additional Information [blank]  Accident Spot Verification Spot Location Address Nana Varachha, Su… |
| 26a1c120-51d0-4299-923f-407cc656a557 | 5 | 218890910_Claim_Form | claim_form | text |  | pe: [checkbox] Savings [checkbox] Current [checkbox] Cash Credit PAN No: [blank]  9. Declaration: 1. I/We the insured named, do hereby, to the best of my/our knowledge and belief, warrant the truth o… |
| 28f75737-98ea-4bf5-b3cf-e82f660045ad | 1 | 223215102_Investigation_Report | correspondence | text |  | asons for Delay Intimation (In case delay is more than 10 days) There is no delay in the intimation. Additional Information Version of Insured on Claim As per the statement provided by the insured, M… |
| 297101e5-012b-4d09-b2f0-058679bf931b | 3 | 223215102_Investigation_Report | correspondence | text |  | shop. They did not take the photographs as they got scared and the IV was in the middle of the road. Vehicle Detail Vehicle Registration Number GJ27AA0736 \| Class of vehicle Private Car Make HYUNDAI… |
| 34ffb262-48c9-4e1d-9a72-7236f1fdd517 | 2 | 223215102_Investigation_Report | correspondence | text |  | On 08-08-2023 after dinner, he and his friend Prakash Chaudhari were going to fill petrol in the IV. When they were passing Nana Varachha in front of Motinagar a motorcycle came from the wrong side s… |
| 357a956e-791b-42b1-b13a-4b761b4c0a33 | 0 | 223233267_Signed_Licensed_Surveyor_Report | accident_report | text |  | Claim No : OC-24-2203-1801-00002660 Registration No : GJ27AA0736  Printed On : 18-SEP-2023 Approval(Annexure-1)  Parts Report Claim Id : 31871257  \| \| QTY \| Retail Price \| Total Amount \| Net Tax… |
| 37795075-78d8-4248-a3ae-25ff73987c7a | 2 | 223233211_Supplier_Bill | repair_estimate | text |  | TTEN: V.M.Desai] VIVEKKUMAR M DESAI Surveyor & Loss Assessor. Lic No: 73760, Valid Upto: 03/10/2024. * Please quote my Ref. Number/Job No. while disbursement of the payment of this bill. Y\2023-2024/… |
| 3997f59e-9cba-47b8-aefd-f0c1e437e112 | 3 | 218890910_Claim_Form | claim_form | text |  | r claim is under Add on endorsement and if Yes provide the details: [checkbox] Yes [checkbox] No  7. Third party vehicle / Injury/Occupant/passenger / Property Details which is involved in the accide… |
| 3a4b03be-a200-4874-8606-7a80c22ddad1 | 3 | 218891028_Policy_Copy | policy_copy | text |  | rule 48, we are not required to prepare an invoice in terms of the provisions of the said sub-rule. For help and more information: Contact our 24 Hour Call Centre at 1800-102-5858, 1888-209-5858, Tol… |
| 3bd0c466-9342-4a5f-bc09-0ea4af62abfb | 2 | 219358654_Repair_Estimate | repair_estimate | text |  | 1.00 23 \| COMPRESSOR ASSY \| 977014N100 \| 9,039.10 \| 1.00 \| 1,627.04 \| 10,666.14  Labour Detail  Seq. \| Labour Description \| Labour Amt \| Qty \| Tax \| Total  1 \| RADIATOR ASSY \| 800.00 \| … |
| 3f0656c9-b805-4892-8b4d-56178fa17b27 | 5 | 223214762_Investigation_Report | correspondence | text |  | ges in correlation with Injuries and Manner of accident The IV has been damaged from the front side. Additional Information [blank]  Accident Spot Verification Spot Location Address Nana Varachha, Su… |
| 42785d70-ecdc-4041-a5d0-c8a36fce0067 | 0 | 222633187_Statement_of_Driver | driver_statement | text |  | [HANDWRITTEN DOCUMENT IN GUJARATI SCRIPT]  Date: 19\|08\|2023  [Header in Gujarati script] B.M. [Text in Gujarati] MO. 8308953545  [Main body - handwritten narrative in Gujarati script, approximately… |
| 42de75f5-a8f6-4c8d-ac0b-f9fa8d2995b8 | 3 | 223214762_Investigation_Report | correspondence | text |  | shop. They did not take the photographs as they got scared and the IV was in the middle of the road. Vehicle Detail Vehicle Registration Number GJ27AA0736 \| Class of vehicle Private Car Make HYUNDAI… |
| 45bfa970-048b-46d9-a2b7-e5203bfb901d | 1 | 223214762_Investigation_Report | correspondence | text |  | asons for Delay Intimation (In case delay is more than 10 days) There is no delay in the intimation. Additional Information Version of Insured on Claim As per the statement provided by the insured, M… |
| 48e97317-6bc8-48fa-a5a2-a095b73fa5f9 | 0 | 222633435_Any_Other | other | text |  | Page 1: [Person writing on document at table with patterned curtains in background]  Page 2: Google account menu screen showing: - Account: prakash Chaudhari - Email: uahachaudhari28@gmail.com - "Man… |
| 496b9b3f-af7e-405b-a234-4fb73363554d | 6 | 223214762_Investigation_Report | correspondence | text |  | rict SURAT \| State GUJARAT \| Pin 0 \| Contact No 0 Version of Eye witness No eyewitness is available. Driver Details Personal meeting with driver Yes \| Reason [blank] Whether Address of driver vis… |
| 4e567837-f49e-4511-93ba-d6251c75aedd | 7 | 223214762_Investigation_Report | correspondence | text |  | informed him that he would have to drive the IV whenever required as he does not know how to drive. On 08-08-2023 at around 21:00 he and his friend were going to fill the petrol in the IV at that tim… |
| 52744898-6fdc-46ba-8c01-fd844aaecc8e | 0 | 222633146_Statement_of_Insured | insured_statement | text |  | [DATE: 19/09/2023]  [HANDWRITTEN TEXT IN GUJARATI SCRIPT]  Document contains handwritten content in Gujarati language. Key visible elements:  - Date notation: 19/09/2023 (top right) - Multiple lines … |
| 53a46ec6-0b0c-40a5-9b00-615f3341a686 | 9 | 223215102_Investigation_Report | correspondence | text |  | his friend was sitting on the co-seat, but because he does not have an MDL he gave his friend's MDL. We have verified at Bappa Sitaram Car Mela and they have confirmed that the IV was purchased on 03… |
| 55a881e5-be75-4d2e-9042-b2b155bc91fc | 4 | 223215102_Investigation_Report | correspondence | text |  | r/ Bill Book [blank]  Garage Details Garage/Repairer Name Navjivan Hyundai Garage Postal Address Nr. SMC south Zone office, DevChand Nagar, Udhana, Surat PO and Village BAMROLI \| District SURAT \| S… |
| 58c092da-d987-4546-9ff2-9b8c8c43f635 | 1 | 219358654_Repair_Estimate | repair_estimate | text |  | UMAR INDRASING VASAVA 6 NANA VARACHHA HOUSING SOC.DHAL NANA VARACHHA KAMREJ SURAT  Part Detail  Seq. \| Part Description \| Part No \| Part Amt \| Qty \| Tax \| Total  1 \| 310 ml-SEALANT KIT-W/S GLA… |
| 5b0e3465-469a-49e6-ba3d-4d7ea3126c86 | 6 | 223237590_Signed_Licensed_Surveyor_Report | accident_report | text |  | sessed Amount (Parts + Labour) : 77942  [HANDWRITTEN SIGNATURE: U.M.Desai] Surveyor Signature  Auth. BAGIC Signature  [CIRCULAR STAMP: Visible in bottom center] |
| 5be6aecb-a11b-42f4-bc2f-544d45b1a251 | 0 | 223721550_Follow-up_Letters | correspondence | text |  | BAJAJ ALLIANZ GENERAL INSURANCE COMPANY LIMITED (A Company incorporated under Indian Companies Act, 1956 and licensed by Insurance Regulatory and Development Authority of India [IRDAI] vide Regd. No.… |
| 5ec5d9b3-4ff5-42c2-b552-493c371bf7bd | 2 | 223721550_Follow-up_Letters | correspondence | text |  | ore rights on our part and all our rights under and in relation to the Policy remain fully reserved. For Grievance Redressal Procedure Visit: https://www.bajajallianz.com/about-us/customer-service.ht… |
| 62adb7a2-62c2-4d78-a889-879ea867c542 | 1 | 218891028_Policy_Copy | policy_copy | text |  | nd licensed by Insurance Regulatory and Development Authority of India [IRDA] vide Reg No.113) Regd. Office: Bajaj Allianz House, Airport Road, Yeravada, Pune-411006(India) PRIVATE CAR PACKAGE POLICY… |
| 664f9732-a5fc-4ac0-ac86-88f40c9b7cec | 10 | 223214762_Investigation_Report | correspondence | text |  | cial Network Analysis Observation on Social Network Analysis [blank]  QC1 Marked Flags Trigger[1] 4. Driver Implant Y IS IV damage on driver side Yes Is driver injury provided No Driver injury detail… |
| 66c53284-e7ba-420d-b02e-7b5315f3e682 | 6 | 218890910_Claim_Form | claim_form | text |  | -submission of the required documents, Company is at liberty to reject the claim as mentioned above. Due to delay in claim's processing/settlement of claim due to claimant's non-fulfillment of requir… |
| 697efc68-1f24-439d-9259-37aebf2fd377 | 7 | 223215102_Investigation_Report | correspondence | text |  | informed him that he would have to drive the IV whenever required as he does not know how to drive. On 08-08-2023 at around 21:00 he and his friend were going to fill the petrol in the IV at that tim… |
| 6a44f33c-9396-4c1f-aaf1-06950144060c | 9 | 223214762_Investigation_Report | correspondence | text |  | his friend was sitting on the co-seat, but because he does not have an MDL he gave his friend's MDL. We have verified at Bappa Sitaram Car Mela and they have confirmed that the IV was purchased on 03… |
| 739fac8d-50ff-40d8-84e9-8395802cfed8 | 0 | 219430367_Pre_Inspection_Photographs_Reports | vehicle_document | text |  | HYUNDAI i10 SPORT 2 BWM  Registration Number: GJ27AA0736  Vehicle Images - Front, Side, Rear Views  Odometer Reading: [visible in dashboard image]  Dashboard Instruments: Speedometer, fuel gauge, tem… |
| 79a515a0-2152-4e19-88fb-1c997127dd2e | 0 | 223214762_Investigation_Report | correspondence | text |  | INVESTIGATION REPORT Report Date : 18-SEP-2023 02:57:46 PM  Claim Detail Claim No OC-24-2203-1801-00002660 \| Policy No OG-24-2203-1801-00005412 Policy Period From 03-AUG-2023 \| Policy Period To 02-… |
| 7d01be7b-b6ab-4c7c-9b79-1cc0af606f47 | 2 | 218890910_Claim_Form | claim_form | text |  | ox] Yes [checkbox] No GD / FIR No: [blank] Place of Accident: [HANDWRITTEN: Nema Vasselley city]  4. Driver Details [Driver driving on the date and time when accident/theft took place for insured veh… |
| 823bba1a-a896-4529-bb3f-25964b3f5668 | 0 | 218890867_Motor_Driving_License_(MDL) | driving_license | text |  | # EXTRACTED TEXT FROM DRIVING LICENCE IMAGE  Form - 7  GUJARAT STATE Driving Licence  Number                          Issued on GJ05/028137/06                  15/04/2006  Name                       … |
| 837b8946-10ac-4b2e-9b07-58048cc69031 | 0 | 218890832_Registration_Certificate | vehicle_document | text |  | GUJARAT MOTOR VEHICLE DEPARTMENT [SURAT] VEHICLE PARTICULARS  Application No: GJ230808V2160368 Registration Date: 17-Oct-2013 Registration No: GJ27AK0736 Previous Registration No: Owner's Name: Son/W… |
| 8a900064-5e5b-4ddf-867c-640065e30116 | 0 | 218891028_Policy_Copy | policy_copy | text |  | BAJAJ ALLIANZ GENERAL INSURANCE COMPANY LIMITED (A Company incorporated under Indian Companies Act, 1956 and licensed by Insurance Regulatory and Development Authority of India [IRDA] vide Reg No.113… |
| 8d4efd2e-8839-4bab-afa3-5d74b7415b2e | 0 | 222633407_Spot_Photo_Sketch | photograph | text |  | STREET SCENE PHOTOGRAPHS - SURAT, INDIA  [Page 1] Urban street scene with mixed commercial and residential buildings. Visible signage includes: - "unacademy" branded auto-rickshaw (blue and black liv… |
| 8e93dc5b-a5ac-4fb5-bda4-05639b08eb77 | 0 | 223215102_Investigation_Report | correspondence | text |  | INVESTIGATION REPORT Report Date : 18-SEP-2023 02:57:46 PM  Claim Detail Claim No OC-24-2203-1801-00002660 \| Policy No OG-24-2203-1801-00005412 Policy Period From 03-AUG-2023 \| Policy Period To 02-… |
| 8f20422e-592b-4e52-9bf5-cf1a126ffb60 | 1 | 223233267_Signed_Licensed_Surveyor_Report | accident_report | text |  | Date: 03-AUG-2023 \| Policy Expiry Date: 02-AUG-2024 Customer Name: MAHESHKUMAR VASAVA \| Vehicle Reg. Number: GJ27AA0736 Telephone No: 9773228144 \| Mobile Number: 9773228144 Customer Address: 6 NAN… |
| 9e320b3e-d224-4832-9a0b-e72ceb6d9496 | 1 | 222633435_Any_Other | other | text |  | ati and English: - Header: "Bupusiraum cabs" with tagline "Drive your dreams" - Contact numbers: Mo. 90793 85368 and Mo. |
| a67fda1a-5fce-43a5-9087-67bb1314f0a2 | 0 | 219032145_Job_Card | payment_slip | text |  | HYUNDAI  Navjivan Motors Pvt. Ltd. (Authorised Sales & Services) Near SMC Ultima South Zone Office, Devchand Nagar, Surat. Tel.: 263 1000, 263 2000, 263 3000, Fax : 263 1010 E-mail : navjivanmotors@g… |
| b33b576c-dd19-4772-bd37-b70cfee61374 | 2 | 218890832_Registration_Certificate | vehicle_document | text |  | nt. Authority Signature is not required. The document can't be used as a MV document in the Vehicle. Vehicle Details (Right Column): Motor Use: 3 No of Cylinders: 3 Engine No: G3H4DM199755 Seating(in… |
| b3991044-d063-415c-b2d3-0eb032da26bd | 0 | 219032034_AML_Documents | pan_card | text |  | # PAN CARD - PERMANENT ACCOUNT NUMBER CARD  **Header (Bilingual):** आयकर विभाग \| INCOME TAX DEPARTMENT भारत सरकार \| GOVT OF INDIA  **Card Type:** स्थायी खाता संख्या कार्ड Permanent Account Number C… |
| b5acec28-3ab5-4ced-b9ff-187dac2a2c46 | 2 | 223237590_Signed_Licensed_Surveyor_Report | accident_report | text |  | 03-AUG-2023 \| Policy Expiry Date \| 02-AUG-2024 \| \| Customer Name \| MAHESHKUMAR VASAVA \| Vehicle Reg. Number \| GJ27AA0736 \| \| Telephone No \| 9773228144 \| Mobile Number \| 9773228144 \| \| C… |
| b9f011dc-bc4a-4229-9edf-9337179a7006 | 1 | 223237590_Signed_Licensed_Surveyor_Report | accident_report | text |  | 8 \| \| \| END ASSY-TIE ROD,RH KO \| 1 \| 608 \| 608 \| 0 \| 608 \| 243.2 \| 364.8 \| \| \| JOINT ASSY-INNER BAL. \| 1 \| 879 \| 879 \| 0 \| 879 \| 351.6 \| 527.4 \| \| \| CARRIER ASSY-FRONT END MODU… |
| be513e9e-4fa4-43c5-8b15-91f516b9b4cd | 3 | 219358654_Repair_Estimate | repair_estimate | text |  | my below in evidence of agreeing to the terms & conditions, given in reverse side of this estimate. Date \| Customer Signature  Terms & Condition given overleaf. |
| beac8d70-d78f-434a-a713-e379d6efde9a | 2 | 218891028_Policy_Copy | policy_copy | text |  | 2-AUG-2024 LL to person for Paid driver/Operation/Maintenance: 50.00 PA Cover For 5 Passenger Of Rs. 100000 each: 250.00 Total Act Premium - B: 2,725.00  **Note: The above Total OD Premium is inclusi… |
| c06009cd-c20f-46d6-a7aa-a3d96e2102b3 | 1 | 222633407_Spot_Photo_Sketch | photograph | text |  | ectural styles - Street-level commercial activity  [Page 2] Empty street/road with concrete surface. Lined with: - Dense green vegetation and trees on both sides - Concrete boundary walls/planters wi… |
| c289ea9b-02ff-48fb-ab3c-0d48ad99b2ea | 0 | 223237590_Signed_Licensed_Surveyor_Report | accident_report | text |  | Claim No : OC-24-2203-1801-00002660 Registration No : GJ27AA0736  Printed On : 18-SEP-2023 Approval(Annexure-1)  Parts Report Claim Id : 31871257  \| \| QTY \| Retail Price \| Total Amount \| Net Tax… |
| c459d91f-5225-4993-b676-b33de923e200 | 2 | 222633435_Any_Other | other | text |  | eader: "Bupusiraum cabs" with tagline "Drive your dreams" - Contact numbers: Mo. 90793 85368 and Mo. 99133 16746 - Form fields visible:   - Vehicle registration number: 9227463964   - Vehicle details… |
| c8de30b3-d6db-4080-a572-225d635e8c65 | 10 | 223215102_Investigation_Report | correspondence | text |  | cial Network Analysis Observation on Social Network Analysis [blank]  QC1 Marked Flags Trigger[1] 4. Driver Implant Y IS IV damage on driver side Yes Is driver injury provided No Driver injury detail… |
| c94183ef-2364-498e-81fc-d91c31d06448 | 0 | 218890942_Claim_Form | correspondence | text |  | List of Documents required for claim settlement (To be submitted to the nearby Bajaj Allianz Office)  For Accident Claim  ☐ Duly filled and signed claim form. ☐ Proof of insurance-Policy/Covermote co… |
| cde9f076-02ea-429d-a209-9c6790dde2f6 | 0 | 222696526_Statement_of_Insured | insured_statement | text |  | [HANDWRITTEN DOCUMENT IN GUJARATI SCRIPT]  Page 1:  [Top right, handwritten in blue ink] દાવો નંબર: [HANDWRITTEN: appears to be a reference number] દિનાંક: [HANDWRITTEN: date] 9227637160  [Main body … |
| d5069fd7-94bf-423d-a67f-b289793e14b3 | 1 | 218890832_Registration_Certificate | vehicle_document | text |  | de policy certificate/covermode no OG-24-2203-1801-0005412 is valid from 03-Aug-2023 to 02-Aug-2024. FIN Details: BAJAJ FINANCE LIMITED, OFFICE 301 TO 311 3RD FL, UNIVERSALBUSINESS CENTER L.P.SAVANI … |
| dbb817f0-a5d4-47f8-aa38-413fff659ec4 | 1 | 222633146_Statement_of_Insured | insured_statement | text |  | pt complexity, detailed character-by-character transcription of Gujarati text requires verification. Key structured elements visible but narrative sections are [HANDWRITTEN: GUJARATI TEXT - REQUIRES … |
| de2eeb82-bfa9-4780-871a-59e798c4b8b9 | 0 | 218890965_Repair_Estimate | repair_estimate | text |  | Navjivan Motors Pvt. Ltd. (Authorised Sales & Services) Near SMC Udhna South Zone Office, Devchand Nagar, Udhna, Surat. Tel. + 91 261-3206002 / 03 E-mail : bodyshop@navjivanhydundai.com Branch Office… |
| e3b586bd-c95e-44ea-80f8-aa227a6ce675 | 4 | 218890910_Claim_Form | claim_form | text |  | Contact Number \| Vehicle Number/Person ID \| Description of Injury / damage [TABLE APPEARS EMPTY]  8. Policy holder / Insured bank NEFT details for claims payment [and thereby agree to submit the or… |
| e4168ae3-45f4-48aa-bb10-931663760212 | 0 | 223233211_Supplier_Bill | repair_estimate | text |  | Vivekkumar M. Desai Surveyor & Loss Assessor (Motor)  Licence No.: S.I.A. 73760 Valid upto: 03rd Oct 2024 Licensiate Membership No.: L/W/06452  Address: 29,Anand Nagar Society, Morabagad, Rander Road… |
| ea720d5e-83a1-4a96-a4a8-f889fe334d81 | 0 | 219358654_Repair_Estimate | repair_estimate | text |  | M/S NAVJIVAN MOTORS PVT.LTD. Repair Estimate  Estimate No : ET23080090 Reg No : GJ27AA0736 Model : EON Type : Insurance  Date : 16.08.2023 VIN : MALA351ALDM226944 Engine No : G3HADM199755 Insurance C… |
| eb2a9bcc-a448-49fb-a3c7-0443c2ef403b | 0 | 222633313_Vehicle_Damage_Photo | photograph | text |  | White Hyundai i10 hatchback vehicle, registration number GJ27AA0736, parked in a parking lot. Multiple photographs showing different angles of the vehicle with visible damage. Page 1: Side view of wh… |
| ebabf627-babc-4d3f-ba6c-2f781d21e8d0 | 3 | 223237590_Signed_Licensed_Surveyor_Report | accident_report | text |  | CHHA, KAM-REJ ROAD, SURAT CITY, SURATGUJARATG395006 \| \| \| \| Repairer Name \| NAVJIVAN MOTORS PVT LTD. \| \| \|  \| Vehicle Information \| \| \| \| \|---\|---\|---\|---\| \| Registration No \| GJ2… |
| ecbedb31-9635-430f-8e83-b0a2a23de9cc | 0 | 219032051_Claim_Form | correspondence | text |  | List of Documents required for claim settlement (To be submitted to the nearby Bajaj Allianz Office)  For Accident Claim  ☐ Duly filled and signed claim form. ☐ Proof of insurance-Policy/Covermote co… |
| f0ed3f21-0b15-402e-9801-eabee2532cd3 | 1 | 218890910_Claim_Form | claim_form | text |  | e read carefully the attached list of documents required for faster and processing of your claim. 2. Policy Holder Details: Policy Number: OC-24-9003-1801-0000 2660 Name of the Insured: [HANDWRITTEN:… |
| f83a796a-7e81-42d1-be27-172eb6dc270e | 4 | 223214762_Investigation_Report | correspondence | text |  | r/ Bill Book [blank]  Garage Details Garage/Repairer Name Navjivan Hyundai Garage Postal Address Nr. SMC south Zone office, DevChand Nagar, Udhana, Surat PO and Village BAMROLI \| District SURAT Stat… |
| f8c0a93f-24c6-4184-82d0-ae44184fefce | 5 | 223237590_Signed_Licensed_Surveyor_Report | accident_report | text |  | ture  Auth. BAGIC Signature  Report Issued without prejudice subject to policy terms and conditions. [CIRCULAR STAMP: Visible in bottom center]  Report Printed On : 18-09-2023 04:51:59  ---  \| \| \|… |
| f9e49d29-169a-4608-9b8b-253d65e92555 | 0 | 218890910_Claim_Form | claim_form | text |  | Bajaj Allianz General Insurance Company Limited Corporate Identity Number: U66010PN2000PLC153329, IRDAI Registration No.113 Regd. Office & Head Office: CE Plaza, Airport Road, Verwada, Pune – 411 005… |
| fcd706c1-5c5f-419f-b59e-c097fe01a74e | 1 | 218890965_Repair_Estimate | repair_estimate | text |  | ed by : _________________________ Reinspection by : _______  \| Sr.No. \| Particulars \| Amount Rs. Ps. \| \|--------\|-------------\|----------------\| \| 1 \| Front Bumper NEW \| APPROVED \| \| 2 \… |
| fddff957-4d80-453b-a8ed-b862b9826c9f | 3 | 222633435_Any_Other | other | text |  | rge signage: "Bupusiraum cabs" with logo - "Drive your dreams" tagline - Contact number visible: Mo. 99133 16746 - Indian flag visible on building - Multiple vehicles parked in lot - Covered showroom… |

## J — Scoring

**J.1 — Rule score**

`rule_score = 92`. Computed by `analysis._score_rules` from each triggered rule's severity weight × confidence, summed and normalised to 0–100. See Section F for the full list.

**J.2 — Similarity score**

`similarity_score = 44`. Computed by `tools.scoring.calculate_similarity_score` from Qdrant top-N matches against past claims: when any matched past claim is `fraud_confirmed`, `score = max_fraud_similarity × 80 + avg_similarity × 20`; otherwise `score = avg_similarity × 50`. Capped at 100.

**J.3 — Graph score**

`graph_score = 100`. Computed by `tools.scoring.calculate_graph_score`. Inputs:
- ring_membership = `True`
- ring_size = `4`
- fraud_confirmed_count = `0`
- connected_claims (count) = `0`
- hub_entities (count) = `15`

Math: `+50` if ring_membership; for each connected claim `weakest_edge_strength(path) × max(0, 20 − distance×5)`; `+min(20, connection_count × 4)`; `+min(15, dedup_hub_count × 5)`; cap at 100.

Edge strengths: CLAIMANT/HAS_PHONE=1.0, INVOLVES_VEHICLE/PERSON=0.9, HAS_ENTITY=0.5, OCCURRED_AT=0.4, REPAIRED_AT=0.3.

**J.4 — Consistency score**

`consistency_score = 0` (where higher = MORE contradictions = higher risk; see Section E). Per contradiction severity: HIGH=25, MEDIUM=15, LOW=5. Sum capped at 100.

**J.5 — ML / LLM holistic score**

`ml_score = 0`. (no LLM holistic metadata stashed on the result).

**J.6 — Fusion + verdict**

Configured weights: `{"rule": 0.3, "similarity": 0.2, "graph": 0.25, "consistency": 0.15, "ml": 0.1}`

Weighted sum (no lift/boost) = `92×0.3 + 44×0.2 + 100×0.25 + 0×0.15 + 0×0.1 = 61.40`

max_signal = `100` (lift to ≥ max_signal × 0.85 if ≥80)
high-signal count = `2` (×1.15 boost if ≥3)
**Final fraud_score (post-lift, post-boost, capped):** `85`

Risk thresholds (configurable via `risk_thresholds_json`): NO_RISK<25, LOW<45, MEDIUM<70, HIGH≥70.
→ **risk_category = `HIGH`**, **recommended_action = `FIELD`**.

> The pipeline does NOT emit a binary fraud / not-fraud flag. The verdict is the (risk_category, recommended_action) pair above. Recommended actions are per `tools.scoring.determine_recommended_action` — TP claims always go FIELD; OD claims map to WAIVER / DESKTOP / FIELD based on risk × claim-amount-vs-high-value-threshold.

## K — Persistence audit

**Postgres / typed tables / audit log:**

| artifact | store | location | found | count |
| --- | --- | --- | --- | --- |
| Classified documents | Postgres | ingest.documents | ✓ | 24 |
| Critical identifiers | Postgres | ingest.critical_identifiers | ⚠ | 0 |
| Facts | Postgres | ingest.facts | ✓ | 546 |
| Contradictions | Postgres | analysis.contradictions | ✓ | 13 |
| Triggered rules | Postgres | analysis.triggered_rules | ✓ | 6 |
| Questions | Postgres | analysis.questions | ✓ | 12 |
| Final result row | Postgres | core.sqc_results | ✓ | 1 |
| Audit log (this completion) | Postgres | core.audit_logs | ✓ | 1 |
| Per-doc-type (police.fir_docs) | Postgres | police.fir_docs | ⚠ | 0 |
| Per-doc-type (police.charge_sheet_docs) | Postgres | police.charge_sheet_docs | ⚠ | 0 |
| Per-doc-type (police.panchnama_docs) | Postgres | police.panchnama_docs | ✗ | err: ProgrammingError |
| Per-doc-type (police.investigation_158_docs) | Postgres | police.investigation_158_docs | ✗ | err: ProgrammingError |
| Per-doc-type (surveyor.investigation_report_docs) | Postgres | surveyor.investigation_report_docs | ⚠ | 0 |
| Per-doc-type (surveyor.repair_estimate_docs) | Postgres | surveyor.repair_estimate_docs | ✗ | err: ProgrammingError |
| Per-doc-type (surveyor.spot_survey_docs) | Postgres | surveyor.spot_survey_docs | ✗ | err: ProgrammingError |
| Per-doc-type (vehicle.rc_book_docs) | Postgres | vehicle.rc_book_docs | ⚠ | 0 |
| Per-doc-type (vehicle.driving_license_docs) | Postgres | vehicle.driving_license_docs | ⚠ | 0 |
| Per-doc-type (vehicle.fitness_certificate_docs) | Postgres | vehicle.fitness_certificate_docs | ✗ | err: ProgrammingError |
| Per-doc-type (financial.bank_statement_docs) | Postgres | financial.bank_statement_docs | ✗ | err: ProgrammingError |
| Per-doc-type (financial.income_proof_docs) | Postgres | financial.income_proof_docs | ⚠ | 0 |
| Per-doc-type (identity.aadhaar_docs) | Postgres | identity.aadhaar_docs | ✗ | err: ProgrammingError |
| Per-doc-type (identity.pan_docs) | Postgres | identity.pan_docs | ✗ | err: ProgrammingError |
| Per-doc-type (general.claim_form_docs) | Postgres | general.claim_form_docs | ✗ | err: ProgrammingError |
| Per-doc-type (general.policy_copy_docs) | Postgres | general.policy_copy_docs | ✗ | err: ProgrammingError |
| Per-doc-type (general.claimant_statement_docs) | Postgres | general.claimant_statement_docs | ✗ | err: ProgrammingError |
| Per-doc-type (general.insured_statement_docs) | Postgres | general.insured_statement_docs | ✗ | err: ProgrammingError |
| Per-doc-type (medical.post_mortem_docs) | Postgres | medical.post_mortem_docs | ⚠ | 0 |
| Per-doc-type (medical.medical_bill_docs) | Postgres | medical.medical_bill_docs | ✗ | err: ProgrammingError |
| Per-doc-type (medical.hospital_admission_docs) | Postgres | medical.hospital_admission_docs | ✗ | err: ProgrammingError |

**Neo4j (outgoing edges from this claim node):**

| rel_type | count |
| --- | --- |
| INVOLVES_PERSON | 25 |
| HAS_PHONE | 21 |
| RELATED_TO | 263 |
| INVOLVES_VEHICLE | 39 |
| OCCURRED_AT | 38 |
| REPAIRED_AT | 2 |
| CLAIMANT | 1 |
| HAS_ENTITY | 117 |

**Qdrant chunks (collection `sqc_document_chunks`):** `79`

**MinIO objects (prefix `claims/OC-24-2203-1801-00002660-INVESTIGATOR6/`):** `48`

**Redis job key (`sqc:job:JOB-B03A0BD4F469`):** `present=True, ttl=86399s`

## L — Redis state

| key | type | semantic | ttl | value preview |
| --- | --- | --- | --- | --- |
| sqc:job:JOB-B03A0BD4F469 | string (JSON) | full job state — status / progress / phase / timestamps | 86399s | {"status": "processing", "claim_id": "OC-24-2203-1801-00002660-INVESTIGATOR6", "progress": 1.0, "created_at": "2026-06-… |
| sqc:cache:*OC-24-2203-1801-00002660-INVESTIGATOR6* | - | (no cache keys for this claim — caches expired or never set) | - | - |

_Redis is **purely transient** in this pipeline — it stores job progress, caches, distributed locks, and rate-limit counters. No authoritative pipeline output lives only in Redis; a Redis flush at any point would lose the progress UI but not the actual claim data (which lives in Postgres / Neo4j / Qdrant / MinIO)._
