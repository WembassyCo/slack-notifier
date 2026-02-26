# Slack Notifier Workflow

n8n workflow for sending Slack notifications via webhook.

## Overview

This replaces the previous Python FastAPI service with a pure n8n workflow approach.

## Quick Start

```bash
# 1. Copy environment template
cp .env.example .env

# 2. Edit .env with your credentials
nano .env

# 3. Configure Slack credentials in n8n UI
# Navigate to http://localhost:5678 after starting
# Settings > Credentials > Add Credential > Slack

# 4. Start n8n
docker-compose up -d

# 5. Import workflow
# Open n8n UI > Workflows > Import from File > Select workflows/slack-notify.json
```

## Usage

### Webhook Endpoint
```
POST http://localhost:5678/webhook/slack-notify
```

### Request Body
```json
{
  "channel": "#general",
  "text": "Hello from Wembassy"
}
```

### Response
```json
{
  "success": true,
  "message": "Slack notification sent",
  "channel": "#general",
  "timestamp": "2026-02-25T22:00:00.000Z"
}
```

## Workflow Nodes

1. **Slack Webhook** - Receives POST requests
2. **Validate Input** - Validates channel and text fields
3. **Send Slack Message** - Sends message via Slack API
4. **Success Response** - Returns success confirmation

## Configuration

### Slack Credentials

1. Create a Slack App at https://api.slack.com/apps
2. Add `chat:write` bot scope
3. Install app to your workspace
4. Copy Bot User OAuth Token to n8n credentials

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| N8N_BASIC_AUTH_USER | Yes | Admin username |
| N8N_BASIC_AUTH_PASSWORD | Yes | Admin password |
| N8N_ENCRYPTION_KEY | Yes | Encryption key |
| WEBHOOK_URL | No | Public webhook URL |

## Testing

```bash
curl -X POST http://localhost:5678/webhook/slack-notify \
  -H "Content-Type: application/json" \
  -d '{"channel":"#general","text":"Test notification"}'
```
