#-----------------------------------------------------------------------------
#                      LlamaIndex Doc Helper - APP
#                       Duplicate Post-Processing
# ---------------------------------------------------------------------------
#
#  Alejandro Ricciardi (Omegapy)
#  created date: 01/05/2024
#
# Credit:
# Udemy - Eden Marco.
# LlamaIndex- Develop LLM powered applications with LlamaIndex:
# https://www.udemy.com/course/lamaindex/
# All the files and folders have been modified from the original source to meet my requirements or to add functionalities to the programs.
# Furthermore, the code lines are heavily commented on; this is a tutorial, after all.
#
# --------------------------------------------------------------------------
#
#  Description:
#  A node processor class that removes duplicates from our nodes
#
# Custom Node Post-Processors, official LlamaIndex Doc:
# https://docs.llamaindex.ai/en/stable/module_guides/querying/node_postprocessors/root.html
#
#----------------------------------------------------------------------------

#--------------------------------------
#            Dependencies
#--------------------------------------
from abc import abstractmethod
from typing import List, Optional
#-- LlamaIndex
from llama_index import QueryBundle
from llama_index.schema import NodeWithScore

#--------------------------------------
#               Class
#--------------------------------------
class DuplicateRemoverNodePostprocessor:
    """Node postprocessor."""

    @abstractmethod
    def postprocess_nodes(
        self, nodes: List[NodeWithScore], query_bundle: Optional[QueryBundle]
    ) -> List[NodeWithScore]:
        """Postprocess nodes."""
        print("_postprocess_nodes enter")

        unique_hashes = set()
        unique_nodes = []

        for node in nodes:
            node_hash = node.node.hash

            if node_hash not in unique_hashes:
                unique_hashes.add(node_hash)
                unique_nodes.append(node)

        return unique_nodes
