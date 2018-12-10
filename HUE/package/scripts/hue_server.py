import sys, os, pwd, grp, signal, time
from resource_management import *
from subprocess import call

class HueServer(Script):
  """
  Contains the interface definitions for methods like install, 
  start, stop, status, etc. for the Hue Server
  """
  def install(self, env):
    # Import properties defined in -config.xml file from params class
	pass
	
  def configure(self, env):
	pass
	
  def start(self, env):
    import params
    #self.stop(env)
#    self.configure(env)
    #Execute(format("/usr/local/hue/hue/hue-4.2.0/build/env/bin/supervisor >> /usr/local/hue/hue/hue-4.2.0/logs/hue-start.log 2>&1 &"),user=params.hue_user
    Execute('/usr/local/hue/hue/hue-4.2.0/hue-server.sh start')
    Execute ('ps -ef | grep hue | grep supervisor | grep -v grep | awk \'{print $2}\' > ' + params.hue_server_pid_file, user=params.hue_user)

  def stop(self, env):
    import params
    #env.set_params(params)
    # Kill the process of Hue
    Execute ('ps -ef | grep hue | grep -v grep | awk  \'{print $2}\' | xargs kill -9')
    #Execute ('rm -rf /usr/local/hue/hue/hue-4.2.0/hue-server.pid')    
    File(params.hue_server_pid_file,
      action = "delete",
      user = params.hue_user
    )

  def status(self, env):
    import status_params
    env.set_params(status_params)
    #use built-in method to check status using pidfile
    check_process_status(status_params.hue_server_pid_file)
	
  def usersync(self, env):
    pass

  def metastoresync(self, env):
    pass
	
if __name__ == "__main__":
  HueServer().execute()
