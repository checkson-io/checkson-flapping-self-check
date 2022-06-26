# checkson-flapping-self-check

This repository creates a Docker image that makes an HTTP request to a URL defined by the
environment variable `FLAPPING_STATE_URL`. This endpoint returns `{"state": true}` and 
`{"state": false}` in an alternating manner. This means that the check also alternates
between successful and unsuccessful runs, so that on each run notifications are sent 
via its configured notification channels.

Additional Checkson checks validate that the notification have been sent out, e.g. this
one here for Slack: https://github.com/checkson-io/checkson-slack-self-check
