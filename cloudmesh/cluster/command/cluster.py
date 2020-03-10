from __future__ import print_function
from cloudmesh.shell.command import command, map_parameters, PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.Shell import Shell
import datetime
import textwrap
from cloudmesh.configuration.Config import Config
from cloudmesh.mongo import DataBaseDecorator
from cloudmesh.inventory.inventory import Inventory
from cloudmesh.mongo.CmDatabase import CmDatabase


class ClusterCommand(PluginCommand):

	# noinspection PyUnusedLocal
	@command
	def do_cluster(self, args, arguments):
		"""
		::

		Usage:
			cluster test
			cluster build --id="[ID]" LABEL
			cluster create --cloud=CLOUD --n=N LABEL
			cluster add --id="[ID]" --all LABEL
			cluster remove --id="[ID]" --all LABEL
			cluster terminate --all LABEL
			cluster info --all --verbose=V LABEL

		This command allows you to create and interact with an available cluster of machines.

		Arguments:
			ID		An existing machine ID to be reserved for the cluster.
			LABEL		The label for the cluster.
			CLOUD		Cloud platform to initialize VMs.
			N			Number of instances to request.
			V			Verbosity level.
			
		Options:
			--id      Specify string containing list of IDs, comma delimited format "id1,id2,...,idx".
			--cloud	Specify cloud platform {AWS, Azure, Openstack}.
			--n		Specify number of VMs to initialize.
			--all		OPTIONAL.  Overrides --id, will pass all machines as an argument.
			--verbose OPTIONAL.  Provides verbosity level for info.

		Description:

			cluster build --id="[ID]" --all LABEL

				Groups together existing machines and reserves them for cluster use.  Pass a comma-delimited list of machine ID's as a string.
				Pass --all to associate all available machines to cluster.
				
			cluster create --cloud=CLOUD --n=N LABEL
				
				Automatically requests VMs from the cloud service requested.
			
			cluster add --id="[ID]" --all LABEL

				Adds given machine IDs to cluster.  Pass --all to associate all available machines to cluster.

			cluster remove --id="[ID]" LABEL
			
				Removes given machine IDs from cluster.  Pass --all to disassociate all machines from cluster.

			cluster terminate --all LABEL

				Terminates all instances associated with the cluster, wipes cluster data.  If --all is passed, terminates all running clusters.

			cluster info --all --verbose=v LABEL

				Retrieves cluster data and machine data associatred with cluster.  Verbosity level 1 provides high-level cluster information
				and list of machines associated.  Verbosity level 2 provides cluster information, machine information and status.  Verbosity 
				level 3 provides all available information.

		"""

		VERBOSE(arguments)

		map_parameters(arguments,
					'test',
					'id',
					'label',
					'cloud',
					'n',
					'v',
					'all',
					'verbose'
					)
		inv = Inventory()
		inv.read()

		config = Config()
		user = config["cloudmesh.profile.user"]

		# cmdb = CmDatabase()
		# cmdb.connect()

		# Prepare machine id's to interact
		machine_ids = arguments.id or []
		
		if arguments.build:
			# Builds and stores a cluster connected to existing machine ids
			pass
		# # TODO Revise to update to correct mongo create/update
		# cmdb.UPDATE(clusters)

		if arguments.create:
			n, label, cloud = arguments.n, arguments.label, arguments.cloud
			
			(textwrap.dedent("""cms vm boot --n={0} \
						--name={1}_[0-{0}]	 \
						--cloud={2}""".format(n, label, cloud)))

			Shell("""cms vm ip inventory {0}[0-{1}]""".format(label, n))

		elif arguments.add:
			pass
		elif arguments.remove:
			pass
		elif arguments.terminate:
			pass
		elif arguments.info:
			pass

		
		print(inv.list())
		#inv.save()
		return ""
