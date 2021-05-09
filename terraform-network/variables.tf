variable "region" {
  default = "us-east-1"
}

variable "app-count" {
  description = "Number of docker containers run"
  default     = 1
}

variable "fargate_cpu" {
  description = "Fargate instace CPU (0.25 vCPU = 256 CPU units)"
  default     = "256"
}

variable "fargate_memory" {
  description = "Fargate instace memory (MiB)"
  default     = "512"
}

variable "image_url" {
  description = "Url Image ecr"
  default     = "123456.dkr.ecr.us-east-1.amazonaws.com/pythonnetwork:latest"
}

variable "name_task" {
  description = "Name task for ecs"
  default     = "telegram_task"
}

