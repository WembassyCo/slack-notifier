# Product Requirements Document
## Slack Notifier n8n Workflow

---

### 1. Goal
Convert the Python FastAPI Slack notification service to a pure n8n workflow that receives webhook requests and sends messages to Slack channels.

---

### 2. Inputs

| Input Source | Data Type | Format | Description |
|--------------|-----------|--------|-------------|
| Webhook POST | JSON | application/json | Channel and message text |

**Request Body:**
```json
{
  "channel": "string (required)",
  "text": "string (required)"
}
```

---

### 3. Outputs

| Output Destination | Data Type | Format | Description |
|--------------------|-----------|--------|-------------|
| Slack API | JSON | application/json | Message sent to channel |
| HTTP Response | JSON | application/json | Success/failure confirmation |

**Success Response:**
```json
{
  "success": true,
  "message": "Slack notification sent",
  "channel": "#general",
  "timestamp": "2026-02-25T22:00:00.000Z"
}
```

---

### 4. Acceptance Criteria

- [x] **AC-001:** Workflow receives POST requests via webhook endpoint
- [x] **AC-002:** Validates required fields (channel, text)
- [x] **AC-003:** Sends message to specified Slack channel
- [x] **AC-004:** Returns JSON response with success status
- [x] **AC-005:** Proper error handling for missing fields
- [x] **AC-006:** Docker compose runs n8n with workflow mounted

---

### 5. Node Specifications

| Node | Type | Purpose |
|------|------|---------|
| Slack Webhook | n8n-nodes-base.webhook | Receive POST requests at /webhook/slack-notify |
| Validate Input | n8n-nodes-base.code | Validate channel and text exist |
| Send Slack Message | n8n-nodes-base.slack | Send message to Slack channel |
| Success Response | n8n-nodes-base.respondToWebhook | Return JSON response |

---

### 6. Security

- Slack token stored in n8n credentials (not in workflow JSON)
- Basic authentication enabled for n8n UI
- Encryption key for credential storage

---

*Version: 1.0.0*
*Converted from Python FastAPI to n8n: 2026-02-25*
