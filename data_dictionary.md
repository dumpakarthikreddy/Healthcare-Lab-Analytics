# Healthcare Laboratory Analytics System

## Data Dictionary

| Column Name | Data Type | Description | Example |
|--------------|-----------|-------------|---------|
| Patient_ID | String | Unique patient identifier | P0001 |
| Patient_Name | String | Full name of patient | Rahul Sharma |
| Age | Integer | Patient age | 45 |
| Gender | String | Male/Female | Male |
| Department | String | Lab department | Biochemistry |
| Lab_Name | String | Laboratory name | City Diagnostic Lab |
| Test_Code | String | Unique test code | CBC001 |
| Test_Name | String | Name of test | Complete Blood Count |
| Sample_Status | String | Sample processing status | Verified |
| Machine_Name | String | Analyzer used | Sysmex XN-1000 |
| Parameter_Name | String | Test parameter | Hemoglobin |
| Parameter_Value | Float | Measured value | 13.5 |
| Unit | String | Measurement unit | g/dL |
| Reference_Range | String | Normal value range | 13.0–17.0 |
| Result_Status | String | Normal/High/Low/Critical | Normal |
| Test_Date | Date | Date of test | 2026-07-24 |
| Test_Time | Time | Time of test | 10:30 AM |