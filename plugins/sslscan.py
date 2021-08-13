from autorecon import ServiceScan

class SSLScan(ServiceScan):

	def __init__(self):
		super().__init__()
		self.name = "SSL Scan"
		self.tags = ['default', 'ssl', 'tls']

	def configure(self):
		self.match_all_service_names(True)
		self.require_ssl(True)

	async def run(self, service):
		if service.protocol == 'tcp' and service.secure:
			await service.execute('sslscan --show-certificate --no-colour {address}:{port} 2>&1', outfile='{protocol}_{port}_sslscan.html')
