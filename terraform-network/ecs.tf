resource "aws_ecs_cluster" "telegram" {
  name = "bot-telegram"
}

data "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"
}
resource "aws_ecs_task_definition" "ecsTaskExecutionRole" {
  family                   = "bot-task"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = var.fargate_cpu
  memory                   = var.fargate_memory
  container_definitions    = <<EOF
  [
    {

      "image": "${var.image_url}",
      "name": "telegram-bot",
      "networkMode": "awsvpc"
    }
  ]
  EOF
}

resource "aws_ecs_service" "telegram" {
  name            = "bot-python"
  cluster         = aws_ecs_cluster.telegram.id
  task_definition = aws_ecs_task_definition.ecsTaskExecutionRole.arn
  desired_count   = 1
  launch_type = "FARGATE"
  network_configuration {
    subnets = [ "subnet-id" ]
    assign_public_ip = true
  }
}