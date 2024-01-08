variable "vpc_cidr" {
  description = "CIDR for the VPC"
  type    = string
  default = "10.0.0.0/16"
}

variable "vpc_tags" {
  description = "Tags for the VPC"
  type = map(string)
  default = {
    Name = "TF_VPC"
  }
}

variable "pub_cidrs" {
  description = "CIDR Blocks for subnets"
  type        = list(string)
  default     = ["10.0.0.0/24", "10.0.1.0/24"]
}