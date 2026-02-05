# Instructions

# Suno API Documentation

## Basic Information

### API Address

- Default Address:

``
https://{BASE_URL}/suno/submit/music
https://{BASE_URL}/suno/fetch

``

## Model Support

### Supported Models

- chirp-v3-0 (Corresponding version v3.0)
- chirp-v3-5 (Corresponding version v3.5 )
- chirp-v4 (Corresponding version v4.0 )
- chirp-auk (Corresponding version v4.5 )
- chirp-v5 (Corresponding version v5.0 )

## Callback notification

- Supports `notify_hook` callback address
- Require:
  - Request method: POST
  - Received data: task data structure

## Usage Steps

### 1. Create a Suno Task

### 2. Query Task Progress

## Data Structure

### Task Object

| Field      | Type   | Example                              | Description                                                                                                                                                    |
| ---------- | ------ | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| task_id    | string | f4a94d75-087b-4bb1-bd45-53ba293faf96 | Task ID                                                                                                                                                        |
| action     | string | MUSIC                                | Task type: MUSIC (generate song), LYRICS (generate lyrics)                                                                                                     |
| status     | string | SUCCESS                              | Task status: NOT_START (not started), SUBMITTED (submitted for processing), QUEUED (queued), IN_PROGRESS (in progress), FAILURE (failed), SUCCESS (successful) |
| submitTime | number | 1689231405854                        | Submission time                                                                                                                                                |
| startTime  | number | 1689231442755                        | Start execution time                                                                                                                                           |
| finishTime | number | 1689231544312                        | Finish time                                                                                                                                                    |
| failReason | string | [Invalid parameter] Invalid value    | Reason for failure (value provided upon failure)                                                                                                               |
| data       | object | -                                    | Specific data: Music (array), Lyrics (single)                                                                                                                  |

### Music Continuation

- Requires passing in the `task_id` parameter to specify the task.
