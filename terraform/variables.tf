# value in secret.tfvars

variable "AWS_ACCESS_KEY" {
  type        = string
  description = "AWS_ACCESS_KEY"
}

variable "AWS_SECRET_KEY" {
  type        = string
  description = "AWS_SECRET_KEY"
}

variable "AWS_REGION" {
  type        = string
  description = "AWS_REGION"
}

variable "AMIS" {
  type        = string
  description = "AMIS"
}
