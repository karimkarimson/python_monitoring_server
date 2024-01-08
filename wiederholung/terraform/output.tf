output "dns_name" {
  description = "The DNS name of the load balancer."
  value       = module.tf_lb.dns_name
}

output "instance_ip" {
  value = module.tf_ec2.instance_public_ips
}
# save public ips to files
resource "local_file" "IPs" {
  count    = length(module.tf_ec2.instance_public_ips)
  content  = module.tf_ec2.instance_public_ips[count.index]
  filename = "data/ip_${count.index}"
}