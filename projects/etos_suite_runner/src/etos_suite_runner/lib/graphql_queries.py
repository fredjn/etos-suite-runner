# Copyright 2020-2022 Axis Communications AB.
#
# For a full list of individual contributors, please see the commit history.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Graphql queries."""
TEST_SUITE_STARTED = """
{
  testSuiteStarted(search:"{'links.type': 'CAUSE', 'links.target': '%s'}") {
    edges {
      node {
        data {
          name
        }
        meta {
          id
        }
      }
    }
  }
}
"""


TEST_SUITE_FINISHED = """
{
  testSuiteFinished(search: "{'links.target': '%s', 'links.type': 'TEST_SUITE_EXECUTION'}" last: 1) {
    edges {
      node {
        data {
          testSuiteOutcome {
            verdict
            conclusion
            description
          }
        }
        meta {
          id
        }
      }
    }
  }
}
"""

ACTIVITY_TRIGGERED = """
{
  activityTriggered(search: "{'links.type': 'CONTEXT', 'links.target': '%s'}", last: 1) {
    edges {
      node {
        meta {
          id
        }
      }
    }
  }
}
"""

ACTIVITY_FINISHED = """
{
  activityFinished(search: "{'links.type': 'ACTIVITY_EXECUTION', 'links.target': '%s'}", last: 1) {
    edges {
      node {
        data {
          activityOutcome {
            conclusion
            description
          }
        }
        meta {
          id
        }
      }
    }
  }
}
"""

ENVIRONMENTS = """
{
  environmentDefined(search:"{'links.type': 'CONTEXT', 'links.target': '%s'}") {
    edges {
      node {
        data {
          name
          uri
        }
        meta {
          id
        }
      }
    }
  }
}
"""


ARTIFACTS = """
{
  artifactCreated(search: "{'meta.id': '%s'}") {
    edges {
      node {
        __typename
        data {
          identity
        }
        meta {
          id
        }
      }
    }
  }
}
"""


TERCC = """
{
  testExecutionRecipeCollectionCreated(search: "{'meta.id': '%s'}") {
    edges {
      node {
        meta {
          id
        }
      }
    }
  }
}
"""
