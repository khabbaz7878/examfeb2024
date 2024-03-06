resource "null_resource" "evenodd" {
  triggers = {
    number = var.number 
  }
  
  provisioner "local-exec" {
    command = "python evenodd.py ${var.number}"
  }
}

output "even_or_odd" {
  value = null_resource.even_odd.triggers.number  
}
