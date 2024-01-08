variable "vpc_cidr" {
  type = string
}
variable "vpc_tags" {
  type = map(string)
}
variable "pub_cidrs" {
  type = list(string)
}
variable "ec2_instance_name" {
  type = string
}
variable "ec2_instance_type" {
  type = string
}
variable "ec2_instance_ami" {
  type = string
}
variable "key_name" {
  type = string
}
