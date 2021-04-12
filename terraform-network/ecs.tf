resource "aws_ecs_cluster" "telegram" {
    name = "bot-telegram"
}

resource "aws_ecs_task_definition" "Bot" {
    family = "bot-task"
    execution_role_arn = "aws_iam_role.ecs_task_execution_role.arn"
    network_mode = "awsvpc"
    requires_compatibilities = [ "FARGATE" ]
    cpu = var.fargate_cpu
    memory = var.fargate_memory
    container_definitions = "value"
}
