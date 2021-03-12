def creds = com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
com.cloudbees.plugins.credentials.common.StandardCredentials.class,
    Jenkins.instance,
    null,
    null
);
for (c in creds) {
  if (c.description.toString().contains("bearer token")) {
  	println(c.id + ": " + c.description + " " + c.secret)
  }
}
