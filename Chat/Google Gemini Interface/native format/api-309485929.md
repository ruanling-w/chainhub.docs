# URL context

## OpenAPI Specification

```yaml
openapi: 3.0.1
info:
  title: ''
  description: ''
  version: 1.0.0
paths:
  /v1beta/models/gemini-2.5-pro:generateContent:
    post:
      summary: URL context
      deprecated: false
      description: >-
        Official Documentation: https://ai.google.dev/gemini-api/docs/url-context?hl=en


        URL context tools allow you to provide more context to your model in the form of URLs. By including URLs in your requests, the model will access content from those web pages (as long as it's not one of the URL types listed in the restrictions section), thus informing your answers and improving their quality.

        URL context tools are suitable for the following tasks:

        Extracting data: Extract specific information such as prices, names, or key findings from multiple URLs.

        Comparing documents: Analyze multiple reports, articles, or PDFs to identify differences and track trends.

        Synthesizing and creating content: Combine information from multiple source URLs to generate accurate summaries, blog posts, or reports.

        Analyzing code and documentation: Point to GitHub codebases or technical documentation to explain code, generate setup instructions, or answer questions.
      tags:
        - Chat/Google Gemini API/Native Format
      parameters:
        - name: key
          in: query
          description: ''
          required: true
          example: '{{YOUR_API_KEY}}'
          schema:
            type: string
        - name: Content-Type
          in: header
          description: ''
          required: true
          example: application/json
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                contents:
                  type: array
                  items:
                    type: object
                    properties:
                      parts:
                        type: array
                        items:
                          type: object
                          properties:
                            text:
                              type: string
              required:
                - contents
            example:
              contents:
                - role: user
                  parts:
                    - text: >-
                        Interpreting this website
                        https://www.youtube.com/watch?v=QCvF8mCPwdQ
              tools:
                - UrlContext: {}
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: object
                properties: {}
          headers: {}
          x-apifox-name: success
      security:
        - bearer: []
      x-apifox-folder: Chat/Google Gemini API/Native Format
      x-apifox-status: developing
      x-run-in-apifox: https://app.apifox.com/web/project/5443236/apis/api-309485929-run
components:
  schemas: {}
  securitySchemes:
    bearer:
      type: http
      scheme: bearer
servers:
  - url: https://api.chainhub.tech
    description: Production Environment
security:
  - bearer: []

```
