# PHP image editing demo

```php
<?php
// Introducing the Composer autoloader
require_once 'vendor/autoload.php';

use GuzzleHttp\Client;

// Test variables
$model = "flux-kontext-max";
$queue = ['prompt' => 'Change to blue'];
$correctedImg = 'scene1.png'; // Image file path

// Create a Guzzle HTTP client
$client = new Client();

// Construct a multipart data array - based on Apifox parameters
$multipart = [
    [
        'name' => 'model',
        'contents' => $model
    ],
    [
        'name' => 'prompt',
        'contents' => $queue['prompt']
    ],
    [
        'name' => 'n',
        'contents' => '1'
    ],
    [
        'name' => 'size',
        'contents' => '1024x1024'
    ],
    [
        'name' => 'response_format',
        'contents' => 'b64_json'
    ]
];

// If there are image files, add file data.
if ($correctedImg !== false && file_exists($correctedImg)) {
    $multipart[] = [
        'name' => 'image',
        'contents' => fopen($correctedImg, 'r'),
        'filename' => basename($correctedImg),
        'headers' => [
            'Content-Type' => 'image/png'
        ]
    ];
    echo "Image files have been added: " . $correctedImg . "\n";
} else {
    echo "Warning: Image file does not exist or path is incorrect. " . $correctedImg . "\n";
}

// Output request information
echo "Model: " . $model . "\n";
echo "Prompt: " . $queue['prompt'] . "\n";
echo "Image file: " . $correctedImg . "\n\n";

// Send HTTP request
try {
    echo "Sending a request to CloudMist AI...\n";

    $response = $client->request('POST', 'https://api.chainhub.tech/v1/images/edits', [
        'headers' => [
            'Authorization' => 'Bearer sk-your-key',
            'Accept' => 'application/json'
        ],
        'multipart' => $multipart,
        'timeout' => 60, // Increase the timeout to 60 seconds
        'debug' => true // Enable debug mode to view request details
    ]);

    // Get Response
    $statusCode = $response->getStatusCode();
    $responseBody = $response->getBody()->getContents();

    echo "Request successful!\n";
    echo "Status code: " . $statusCode . "\n";
    echo "Response content:\n" . $responseBody . "\n";

    // Parsing JSON response
    $responseData = json_decode($responseBody, true);
    if (isset($responseData['data']) && isset($responseData['data'][0]['url'])) {
        echo "\nThe generated image URL " . $responseData['data'][0]['url'] . "\n";
    }

} catch (GuzzleHttp\Exception\ClientException $e) {
    echo "Client error (4xx): " . $e->getMessage() . "\n";
    echo "Response content: " . $e->getResponse()->getBody()->getContents() . "\n";
} catch (GuzzleHttp\Exception\ServerException $e) {
    echo "Server error (5xx): " . $e->getMessage() . "\n";
    echo "Response content: " . $e->getResponse()->getBody()->getContents() . "\n";
} catch (Exception $e) {
    echo "Request failed: " . $e->getMessage() . "\n";
}
```
