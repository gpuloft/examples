// Streaming chat completion against GPULoft with the OpenAI Node SDK.
import 'dotenv/config'
import OpenAI from 'openai'

const client = new OpenAI({ baseURL: process.env.GPULOFT_BASE_URL, apiKey: process.env.GPULOFT_API_KEY })

const stream = await client.chat.completions.create({
  model: 'qwen2.5-72b-instruct',
  messages: [{ role: 'user', content: 'Write a haiku about GPUs.' }],
  stream: true,
})
for await (const chunk of stream) process.stdout.write(chunk.choices[0]?.delta?.content ?? '')
process.stdout.write('\n')
