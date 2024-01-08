module "tf_vpc" {
  vpc_cidr  = var.vpc_cidr
  vpc_tags  = var.vpc_tags
  pub_cidrs = var.pub_cidrs
  source    = "./modules/vpc"
}

module "tf_ec2" {
  source            = "./modules/ec2"
  ec2_instance_name = var.ec2_instance_name
  ec2_instance_type = var.ec2_instance_type
  ec2_instance_ami  = var.ec2_instance_ami
  key_name          = var.key_name

  vpc_id    = module.tf_vpc.vpc_id
  subnet_id = module.tf_vpc.pub_sub_id
}

module "tf_lb" {
  source      = "./modules/loadbalancer"
  subnets     = module.tf_vpc.pub_sub_id
  sg_id       = module.tf_ec2.sg_id
  vpc_id      = module.tf_vpc.vpc_id
  instance_id = module.tf_ec2.ec2_id
}
