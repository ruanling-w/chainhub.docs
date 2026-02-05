# Parameters

## Music Generation Parameter Description

### 1. Custom Creation Mode - Normal Generation

| Parameter Name  | Type   | Description           | Remarks                                                                                                     |
| --------------- | ------ | --------------------- | ----------------------------------------------------------------------------------------------------------- |
| title           | String | Music title           | -                                                                                                           |
| tags            | String | Music style           | Separated by commas                                                                                         |
| generation_type | String | Generation type       | Defaults to TEXT                                                                                            |
| prompt          | String | Music creation prompt | Including but not limited to lyrics                                                                         |
| negative_tags   | String | Unwanted styles       | Can be an empty string                                                                                      |
| mv              | String | Model                 | Defaults to chirp-v4<br>Optional: chirp-v3-5, chirp-v3-0<br>Extended for uploading audio: chirp-v3-5-upload |
| metadata        | Object | Custom parameters     | Includes create_mode: custom, vocal_gender: "m"/"f" where m is male and f is female                         |

### 2. Custom Creation Mode - Continuation

| Parameter Name   | Type   | Description           | Remarks                                                            |
| ---------------- | ------ | --------------------- | ------------------------------------------------------------------ |
| title            | String | Music title           | -                                                                  |
| tags             | String | Music style           | Separated by commas                                                |
| generation_type  | String | Generation type       | Defaults to TEXT                                                   |
| prompt           | String | Music creation prompt | Including but not limited to lyrics                                |
| negative_tags    | String | Unwanted styles       | Can be an empty string                                             |
| mv               | String | Model                 | Defaults to chirp-v4<br>Optional: chirp-v3-5, chirp-v3-0           |
| continue_at      | Float  | Continue start time   | From which second to continue creation<br>Example: 120.00 or 61.59 |
| continue_clip_id | String | Continue song ID      | The ID of the song to continue creation                            |
| task             | String | Task type             | Defaults to extend                                                 |

### 3. Custom Creation Mode - Upload and Generate

| Parameter Name           | Type   | Description                    | Remarks                                                                        |
| ------------------------ | ------ | ------------------------------ | ------------------------------------------------------------------------------ |
| prompt                   | String | Music creation prompt          | Can be an empty string                                                         |
| generation_type          | String | Generation type                | Defaults to TEXT                                                               |
| tags                     | String | Music style                    | Separated by commas                                                            |
| negative_tags            | String | Unwanted styles                | Can be an empty string                                                         |
| mv                       | String | Model                          | Please use chirp-v3-5-tau                                                      |
| title                    | String | Music title                    | -                                                                              |
| continue_clip_id         | String | Continued song ID              | Optional parameter, can be null                                                |
| continue_at              | Float  | Continued start time           | Optional parameter, can be null                                                |
| continued_aligned_prompt | String | Continued alignment prompt     | Optional parameter, can be null                                                |
| infill_start_s           | Float  | Infill start time (seconds)    | Optional parameter, can be null                                                |
| infill_end_s             | Float  | Fill in the end time (seconds) | Optional parameter, can be null                                                |
| task                     | String | Task type                      | Use the Cover function, fixed as cover                                         |
| cover_clip_id            | String | Cover ID                       | The ID of the original song to be covered or the ID of the uploaded audio clip |
