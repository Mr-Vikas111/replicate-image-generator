from pydantic import BaseModel, Field
from typing import Optional,List

# Base Input
class ImageInput(BaseModel):
    prompt: str = Field(default="RAW photo, a portrait photo of a latina woman in casual clothes, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3", example="RAW photo, a portrait photo of a latina woman in casual clothes, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3")

class FineTuneInput(BaseModel):
    prompt: str = Field(..., example="m1st1c,\\n\\nA majestic lion with dragon wings and a mane that glows like a sunset, standing proudly on a cliff overlooking a magical forest.\\n\\n, in the style of m1st1c")

# Request Input
class GenerateImageRequest(BaseModel):
    input: ImageInput

class FineTuneImageRequest(BaseModel):
    input: FineTuneInput
    

""" ############################################ RESPONSE SCHEMA FOR GENERATE IMAGE ######################### """

class GenerateMetrics(BaseModel):
    predict_time: float = Field(default=0.0, example=4.49)
    total_time: float = Field(default=0.0, example=4.50)

class GenerateImageInput(BaseModel):
    seed: int = Field(default=0, example=1335)
    steps: int = Field(default=20, example=20)
    width: int = Field(default=512, example=512)
    height: int = Field(default=728, example=728)
    prompt: str = Field(default="A portrait photo of a woman.", example="RAW photo, a portrait photo of a latina woman in casual clothes, natural skin, 8k uhd, high quality, film grain, Fujifilm XT3")
    guidance: int = Field(default=5, example=5)
    scheduler: str = Field(default="EulerA", example="EulerA")
    negative_prompt: str = Field(default="", example="(deformed iris, deformed pupils, semi-realistic, etc.)")


class GenerateUrls(BaseModel):
    get: str = Field(default="", example="https://api.replicate.com/v1/predictions/7y7jvktbl3pwztrtdpg3is5eom")
    cancel: str = Field(default="", example="https://api.replicate.com/v1/predictions/7y7jvktbl3pwztrtdpg3is5eom/cancel")


class GenerateImageRequestResponse(BaseModel):
    completed_at: str = Field(default="", example="2023-08-18T02:01:48.413697Z")
    created_at: str = Field(default="", example="2023-08-18T02:01:43.917126Z")
    data_removed: bool = Field(default=False)
    error: Optional[str] = Field(default=None)
    id: str = Field(default="", example="7y7jvktbl3pwztrtdpg3is5eom")
    input: GenerateImageInput
    logs: str = Field(default="", example="0%|          | 0/20 [00:00<?, ?it/s]")
    metrics: GenerateMetrics
    output: str = Field(default="", example="https://replicate.delivery/pbxt/eVMzXJerAzpqnErNJ9P4ncWmd2d3OkGA31DKhG3ElQhLMIbRA/output.png")
    started_at: str = Field(default="", example="2023-08-18T02:01:43.919215Z")
    status: str = Field(default="succeeded", example="succeeded")
    urls: GenerateUrls
    version: str = Field(default="", example="8aeee50b868f06a1893e3b95a8bb639a8342e846836f3e0211d6a13c158505b1")


""" ############################################ RESPONSE SCHEMA FOR FINE-TUNE IMAGE ######################### """

class GenerateImageFineTuneInput(BaseModel):
    model: str = Field(default="dev", example="dev")
    prompt: str = Field(default="A beautiful landscape.", example="m1st1c,\n\nA majestic lion with dragon wings and a mane that glows like a sunset, standing proudly on a cliff overlooking a magical forest.\n\n, in the style of m1st1c")
    lora_scale: float = Field(default=1.0, example=1.0)
    num_outputs: int = Field(default=1, example=1)
    aspect_ratio: str = Field(default="1:1", example="1:1")
    output_format: str = Field(default="webp", example="webp")
    guidance_scale: float = Field(default=3.5, example=3.5)
    output_quality: int = Field(default=80, example=80)
    extra_lora_scale: float = Field(default=0.8, example=0.8)
    num_inference_steps: int = Field(default=28, example=28)

class GenerateFineTuneRequestResponse(BaseModel):
    completed_at: str = Field(default="", example="2024-08-24T11:20:05.068428Z")
    created_at: str = Field(default="", example="2024-08-24T11:19:43.315000Z")
    data_removed: bool = Field(default=False)
    error: Optional[str] = Field(default=None)
    id: str = Field(default="", example="0znffyghtdrm40chggerbcvb00")
    input: GenerateImageFineTuneInput
    logs: str = Field(default="", example="Using seed: 36832\nPrompt: m1st1c...")
    metrics: GenerateMetrics
    output: List[str] = Field(default_factory=list, example=["https://replicate.delivery/yhqm/eqGlJuqLGvRmJSS513JvfrZ0xMYQNem7aBZV5AeJKEfi85uaC/out-0.webp"])
    started_at: str = Field(default="", example="2024-08-24T11:19:46.091043Z")
    status: str = Field(default="succeeded", example="succeeded")
    urls: GenerateUrls
    version: str = Field(default="", example="294de709b06655e61bb0149ec61ef8b5d3ca030517528ac34f8252b18b09b7ad")
