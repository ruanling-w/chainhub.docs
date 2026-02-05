# Status Codes

// VEO Task Status Constants
const (
VeoStatusPending                  = "pending"
VeoStatusImageDownloading         = "image\_downloading"
VeoStatusVideoGenerating          = "video\_generating"
VeoStatusVideoGenerationCompleted = "video\_generation\_completed"
VeoStatusVideoGenerationFailed    = "video\_generation\_failed"
VeoStatusVideoUpsampling          = "video\_upsampling"
VeoStatusVideoUpsamplingCompleted = "video\_upsampling\_completed"
VeoStatusVideoUpsamplingFailed    = "video\_upsampling\_failed"
VeoStatusCompleted                = "completed"
VeoStatusFailed                   = "failed"
VeoStatusError                    = "error" // Error (used for error responses)
)
