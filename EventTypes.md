# List of Event Types
This shows the list of event types (and their default stream IDs), along with an example of what their content is like.

## VEKG
Default stream id: None (used across all services in the dataflow)
Example:
```json
{
  "id": "publisher1-21c77b46-9a14-4c0e-b75b-02c7136b9fd4",
  "publisher_id": "publisher1",
  "source": "rtmp://172.17.0.1:1934/live/mystream",
  "image_url": "f684f154-9f84-4a36-864a-4de7f03c9501",
  "vekg": {
    "nodes": [
      [
        "86fdb47c-f32f-4b7f-ad43-a068d5f7a228",
        {
          "id": "86fdb47c-f32f-4b7f-ad43-a068d5f7a228",
          "label": "person",
          "confidence": 0.8873831033706665,
          "bounding_box": [
            165,
            40,
            582,
            480
          ]
        }
      ]
    ]
  },
  "query_ids": [
    "a04e8f33c7a272477e0e6779afd84a5b"
  ],
  "width": 720,
  "height": 480,
  "color_channels": "BGR",
  "frame_index": 348,
  "tracer": {
    "headers": {
      "uber-trace-id": "91293b131d2f2f0b:ef925dc04992ce91:d305996bcbeb3eca:1"
    }
  },
  "buffer_stream_key": "ecc611480b5ba2c41d3b49cb8b36600e",
  "data_flow": [
    [
      "object-detection-ssd-gpu-data"
    ],
    [
      "wm-data"
    ]
  ],
  "data_path": [
    "object-detection-ssd-gpu-data"
  ]
}
```
## VEKG_STREAM
Default stream id: None (used across all services in the dataflow)
Example:
```json
{
  "id": "Matcher:ce4d3654-e873-4fe5-b271-cc026f7c89ec",
  "vekg_stream": [
    {
      "id": "publisher1-21c77b46-9a14-4c0e-b75b-02c7136b9fd4",
      "publisher_id": "publisher1",
      "source": "rtmp://172.17.0.1:1934/live/mystream",
      "image_url": "f684f154-9f84-4a36-864a-4de7f03c9501",
      "vekg": {
        "nodes": [
          [
            "86fdb47c-f32f-4b7f-ad43-a068d5f7a228",
            {
              "id": "86fdb47c-f32f-4b7f-ad43-a068d5f7a228",
              "label": "person",
              "confidence": 0.8873831033706665,
              "bounding_box": [
                165,
                40,
                582,
                480
              ]
            }
          ]
        ]
      },
      "query_ids": [
        "a04e8f33c7a272477e0e6779afd84a5b"
      ],
      "width": 720,
      "height": 480,
      "color_channels": "BGR",
      "frame_index": 348,
      "tracer": {
        "headers": {
          "uber-trace-id": "91293b131d2f2f0b:ef925dc04992ce91:d305996bcbeb3eca:1"
        }
      },
      "buffer_stream_key": "ecc611480b5ba2c41d3b49cb8b36600e",
      "data_flow": [
        [
          "object-detection-ssd-gpu-data"
        ],
        [
          "wm-data"
        ]
      ],
      "data_path": [
        "object-detection-ssd-gpu-data"
      ]
    }
  ],
  "query_id": "a04e8f33c7a272477e0e6779afd84a5b",
  "match_return": {
    "is_empty": false,
    "node_ids": [],
    "nodes": {},
    "edges": {},
    "primitives": {
      "PeopleCount": [
        1
      ]
    }
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "91293b131d2f2f0b:ffbd7e7198251f5f:65913fbedf02e924:1"
    }
  }
}
```


## QUERY_RECEIVED
Default stream id: QueryReceived
Example:
```json
{
  "subscriber_id": "sub_id",
  "query": "REGISTER QUERY countPeople OUTPUT AnnotatedVideoStream CONTENT ObjectDetection MATCH (p:person) FROM publisher1 WITHIN TUMBLING_COUNT_WINDOW(1) WITH_QOS accuracy = 'medium_importance', latency = 'medium_high_importance', energy_consumption = 'high_importance' RETURN count(distinct p) as PeopleCount",
  "id": "AccessPoint:eb1f9aab-87cf-4f7d-9fcb-e64c2e6c7103",
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:78bf5b52e81f0e4a:93d62cc33437586f:1"
    }
  }
}
```

## QUERY_CREATED
Default stream id: QueryCreated
Example:
```json
{
  "subscriber_id": "sub_id",
  "query_id": "a04e8f33c7a272477e0e6779afd84a5b",
  "parsed_query": {
    "name": "countPeople",
    "output": [
      "AnnotatedVideoStream"
    ],
    "from": [
      "publisher1"
    ],
    "content": [
      "ObjectDetection"
    ],
    "match": "MATCH (p:person)",
    "optional_match": "",
    "where": "",
    "window": {
      "window_type": "TUMBLING_COUNT_WINDOW",
      "args": [
        1
      ]
    },
    "ret": "RETURN count(distinct p) as PeopleCount",
    "qos_policies": {
      "accuracy": "medium_importance",
      "latency": "medium_high_importance",
      "energy_consumption": "high_importance"
    }
  },
  "query_received_event_id": "AccessPoint:eb1f9aab-87cf-4f7d-9fcb-e64c2e6c7103",
  "buffer_stream": {
    "publisher_id": "publisher1",
    "buffer_stream_key": "ecc611480b5ba2c41d3b49cb8b36600e",
    "source": "rtmp://172.17.0.1:1934/live/mystream",
    "resolution": "720x480",
    "fps": "15"
  },
  "service_chain": [
    "ObjectDetection"
  ],
  "id": "ClientManager:eb8d0d18-f675-4d59-a79f-78b536db51e3",
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:9634259a7670e162:267859ac59353050:1"
    }
  }
}
```


## QUERY_DELETION_REQUESTED
Default stream id: QueryDeletionRequested
Example:
```json
{
    "id": "AccessPoint:eb1f9aab-87cf-4f7d-9fcb-e64c2e6c7103",
    "subscriber_id": "sub_id",
    "query_name": "countPeople",
}
```


## QUERY_REMOVED
Default stream id: QueryRemoved
Example:
```json
{
  "deleted": true,
  "subscriber_id": "sub_id",
  "query_id": "a04e8f33c7a272477e0e6779afd84a5b",
  "parsed_query": {
    "name": "countPeople",
    "output": [
      "AnnotatedVideoStream"
    ],
    "from": [
      "publisher1"
    ],
    "content": [
      "ObjectDetection"
    ],
    "match": "MATCH (p:person)",
    "optional_match": "",
    "where": "",
    "window": {
      "window_type": "TUMBLING_COUNT_WINDOW",
      "args": [
        1
      ]
    },
    "ret": "RETURN count(distinct p) as PeopleCount",
    "qos_policies": {
      "accuracy": "medium_importance",
      "latency": "medium_high_importance",
      "energy_consumption": "high_importance"
    }
  },
  "query_received_event_id": "AccessPoint:eb1f9aab-87cf-4f7d-9fcb-e64c2e6c7103",
  "buffer_stream": {
    "publisher_id": "publisher1",
    "buffer_stream_key": "ecc611480b5ba2c41d3b49cb8b36600e",
    "source": "rtmp://172.17.0.1:1934/live/mystream",
    "resolution": "720x480",
    "fps": "15"
  },
  "service_chain": [
    "ObjectDetection"
  ],
  "id": "ClientManager:eb8d0d18-f675-4d59-a79f-78b536db51e3",
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:9634259a7670e162:267859ac59353050:1"
    }
  }
}
```

## PUBLISHER_CREATED
Default stream id: PublisherCreated
Example:
```json
{
  "publisher_id": "publisher1",
  "source": "rtmp://172.17.0.1:1934/live/mystream",
  "stream_key": "pub-cmd-publisher1",
  "meta": {
    "color": "True",
    "fps": "15",
    "resolution": "720x480"
  },
  "id": "AccessPoint:1e8b3d07-0405-42cd-ba62-67f42b8e3a70",
  "tracer": {
    "headers": {
      "uber-trace-id": "29e2efeda598b708:f34e3fc9adb89f69:671e9ec438824628:1"
    }
  }
}
```

## PUBLISHER_REMOVED
Default stream id: PublisherRemoved
Example:
```json
{
  "publisher_id": "publisher1",
  "id": "AccessPoint:1e8b3d07-0405-42cd-ba62-67f42b8e3a71",
  "tracer": {
    "headers": {
      "uber-trace-id": "29e2efeda598b708:f34e3fc9adb89f69:671e9ec438824628:2"
    }
  }
}
```

## SERVICE_WORKER_ANNOUNCED
Default stream id: ServiceWorkerAnnounced
Example:
```json
{
  "id": "ObjectDetectionService:17e276a8-2dd3-4b0c-a57e-217a68969ecd",
  "worker": {
    "service_type": "ObjectDetection",
    "stream_key": "object-detection-ssd-gpu-data",
    "queue_limit": 100,
    "throughput": 34.33,
    "accuracy": 0.21,
    "energy_consumption": 163.0,
    "content_types": [
      "node_attribute:bounding_box",
      "node_attribute:label",
      "node_attribute:confidence",
      "node:person",
      "node:car"
    ]
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "a32a2a26f8fba7d9:f3650c2cd2987dfc:71a8208bda079a7a:1"
    }
  }
}
```


## SERVICE_SLR_PROFILES_RANKED
Default stream id: ServiceSLRProfilesRanked
Example:
```json
{
  "id": "SLRWorkerRanking:033e4845-923f-4dfc-96cd-9b7ff018a100",
  "service_type": "ObjectDetection",
  "slr_profiles": {
    "ObjectDetection-[0.7, 0.9, 1.0]-[0.5, 0.7, 0.9]-[0.3, 0.5, 0.7]": {
      "query_ids": [
        "a04e8f33c7a272477e0e6779afd84a5b"
      ],
      "criteria_weights": [
        [
          0.7,
          0.9,
          1.0
        ],
        [
          0.5,
          0.7,
          0.9
        ],
        [
          0.3,
          0.5,
          0.7
        ]
      ],
      "alternatives_ids": [
        "object-detection-ssd-gpu-data"
      ],
      "ranking_index": [
        0
      ],
      "ranking_scores": [
        0
      ]
    }
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:936b2a63c5c37884:de5058a938f27734:1"
    }
  }
}
```

## WORKER_PROFILE_RATED
Default stream id: WorkerProfileRated
Example:
```json
{
  "worker": {
    "service_type": "ObjectDetection",
    "stream_key": "object-detection-ssd-gpu-data",
    "energy_consumption": [
      7,
      9,
      10
    ],
    "throughput": [
      7,
      9,
      10
    ],
    "accuracy": [
      7,
      9,
      10
    ]
  },
  "id": "WorkerProfileRating:51c03c59-25ac-4937-adcd-ee3dcb992dde",
  "tracer": {
    "headers": {
      "uber-trace-id": "a32a2a26f8fba7d9:1ba982e2a1720699:69b1d5ee291953f:1"
    }
  }
}
```

## QUERY_SERVICES_QOS_CRITERIA_RANKED
Default stream id: QueryServicesQoSRanked
Example:
```json
{
  "query_id": "a04e8f33c7a272477e0e6779afd84a5b",
  "required_services": [
    "ObjectDetection"
  ],
  "qos_rank": {
    "accuracy": [
      0.3,
      0.5,
      0.7
    ],
    "throughput": [
      0.5,
      0.7,
      0.9
    ],
    "energy_consumption": [
      0.7,
      0.9,
      1.0
    ]
  },
  "id": "QueryPlanner:2f25e909-d222-49c5-b7db-11becdde4a27",
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:1764dea0f879ea5e:1b3a575a57bba47f:1"
    }
  }
}
```


## REPEAT_MONITOR_STREAMS_SIZE_REQUESTED
Default stream id: RepeatMonitorStreamsSizeRequested
Example:
```json
{
  "id": "AdaptationMonitor:ad8a1e5d-f44a-4ff2-bb6a-28ab75397b06",
  "repeat_after_time": 1
}
```

## SERVICE_WORKERS_STREAM_MONITORED
Default stream id: ServiceWorkersStreamMonitored
Example:
```json
{
  "service_workers": {
    "ObjectDetection": {
      "workers": {
        "object-detection-ssd-gpu-data": {
          "service_type": "ObjectDetection",
          "stream_key": "object-detection-ssd-gpu-data",
          "queue_limit": 100,
          "throughput": 34.33,
          "accuracy": 0.21,
          "energy_consumption": 163.0,
          "content_types": [
            "node_attribute:bounding_box",
            "node_attribute:label",
            "node_attribute:confidence",
            "node:person",
            "node:car"
          ],
          "queue_size": 14,
          "queue_space": 86,
          "queue_space_percent": 0.86
        }
      },
      "total_number_workers": 1
    }
  },
  "id": "AdaptationMonitor:51fbf8ad-9bfd-4d0e-87d8-7e87719716be",
  "tracer": {
    "headers": {
      "uber-trace-id": "19d4836b090c339a:ed4a69404fa31b2d:5d24ee4e793516fa:1"
    }
  }
}
```


## NEW_QUERY_SCHEDULING_PLAN_REQUESTED
Default stream id: NewQuerySchedulingPlanRequested
Example:
```json
{
  "id": "AdaptationAnalyser:e2b303c3-1950-4445-b504-e9bdf2528a06",
  "change": {
    "type": "NewQuerySchedulingPlanRequested",
    "cause": {
      "subscriber_id": "sub_id",
      "query_id": "a04e8f33c7a272477e0e6779afd84a5b",
      "parsed_query": {
        "name": "countPeople",
        "output": [
          "AnnotatedVideoStream"
        ],
        "from": [
          "publisher1"
        ],
        "content": [
          "ObjectDetection"
        ],
        "match": "MATCH (p:person)",
        "optional_match": "",
        "where": "",
        "window": {
          "window_type": "TUMBLING_COUNT_WINDOW",
          "args": [
            1
          ]
        },
        "ret": "RETURN count(distinct p) as PeopleCount",
        "qos_policies": {
          "accuracy": "medium_importance",
          "latency": "medium_high_importance",
          "energy_consumption": "high_importance"
        }
      },
      "query_received_event_id": "AccessPoint:eb1f9aab-87cf-4f7d-9fcb-e64c2e6c7103",
      "buffer_stream": {
        "publisher_id": "publisher1",
        "buffer_stream_key": "ecc611480b5ba2c41d3b49cb8b36600e",
        "source": "rtmp://172.17.0.1:1934/live/mystream",
        "resolution": "720x480",
        "fps": "15"
      },
      "service_chain": [
        "ObjectDetection"
      ],
      "id": "ClientManager:eb8d0d18-f675-4d59-a79f-78b536db51e3",
      "tracer": {
        "headers": {
          "uber-trace-id": "4075e6ac22a8af8a:9634259a7670e162:267859ac59353050:1"
        }
      }
    },
    "timestamp": 1740326086.824306
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:599a75e41a1db057:89bf3422ed0ce614:1"
    }
  }
}
```

## SERVICE_WORKER_SLR_PROFILE_CHANGE_PLAN_REQUESTED
Default stream id: ServiceWorkerSLRProfileChangePlanRequested
Example:
```json
{
  "id": "AdaptationAnalyser:a44ebd77-aae3-4f15-97fb-ae0df936398f",
  "change": {
    "type": "ServiceWorkerSLRProfileChangePlanRequested",
    "cause": {
      "id": "SLRWorkerRanking:033e4845-923f-4dfc-96cd-9b7ff018a100",
      "service_type": "ObjectDetection",
      "slr_profiles": {
        "ObjectDetection-[0.7, 0.9, 1.0]-[0.5, 0.7, 0.9]-[0.3, 0.5, 0.7]": {
          "query_ids": [
            "a04e8f33c7a272477e0e6779afd84a5b"
          ],
          "criteria_weights": [
            [
              0.7,
              0.9,
              1.0
            ],
            [
              0.5,
              0.7,
              0.9
            ],
            [
              0.3,
              0.5,
              0.7
            ]
          ],
          "alternatives_ids": [
            "object-detection-ssd-gpu-data"
          ],
          "ranking_index": [
            0
          ],
          "ranking_scores": [
            0
          ]
        }
      },
      "tracer": {
        "headers": {
          "uber-trace-id": "4075e6ac22a8af8a:936b2a63c5c37884:de5058a938f27734:1"
        }
      }
    },
    "timestamp": 1740326086.827682
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:baafa5f60cb28f6f:834009513e7fd945:1"
    }
  }
}
```

## SERVICE_WORKER_OVERLOADED_PLAN_REQUESTED
Default stream id: ServiceWorkerOverloadedPlanRequested
Example:
```json
{
  "id": "AdaptationAnalyser:ac11d6e2-073c-4269-94ca-02d688cb961c",
  "change": {
    "type": "ServiceWorkerOverloadedPlanRequested",
    "cause": {
      "service_workers": {
        "ObjectDetection": {
          "workers": {
            "object-detection-ssd-gpu-data": {
              "service_type": "ObjectDetection",
              "stream_key": "object-detection-ssd-gpu-data",
              "queue_limit": 100,
              "throughput": 34.33,
              "accuracy": 0.21,
              "energy_consumption": 163.0,
              "content_types": [
                "node_attribute:bounding_box",
                "node_attribute:label",
                "node_attribute:confidence",
                "node:person",
                "node:car"
              ],
              "queue_size": 0,
              "queue_space": 100,
              "queue_space_percent": 1.0
            },
            "object-detection-ssd-data": {
              "service_type": "ObjectDetection",
              "stream_key": "object-detection-ssd-data",
              "queue_limit": 100,
              "throughput": 45.6,
              "accuracy": 0.21,
              "energy_consumption": 128.0,
              "content_types": [
                "node_attribute:bounding_box",
                "node_attribute:label",
                "node_attribute:confidence",
                "node:person",
                "node:car"
              ],
              "queue_size": 457,
              "queue_space": -357,
              "queue_space_percent": -3.57
            }
          },
          "total_number_workers": 2
        }
      },
      "id": "AdaptationMonitor:4fea0dda-e84e-4d80-ad45-70f452914ee2",
      "tracer": {
        "headers": {
          "uber-trace-id": "96055a9004ce72c4:f2e0edd965c1951c:d42fafd6de1ce2f8:1"
        }
      }
    },
    "timestamp": 1740330065.194519
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "96055a9004ce72c4:893da3d91daeaa3f:a3c35182b868be2f:1"
    }
  }
}
```

## SERVICE_WORKER_BEST_IDLE_REQUESTED
Default stream id: ServiceWorkerBestIdlePlanRequested
Example:
```json
{
  "id": "AdaptationAnalyser:45897698-f39c-4030-8582-f699d8eda592",
  "change": {
    "type": "ServiceWorkerBestIdlePlanRequested",
    "cause": {
      "service_workers": {
        "ObjectDetection": {
          "workers": {
            "object-detection-ssd-gpu-data": {
              "service_type": "ObjectDetection",
              "stream_key": "object-detection-ssd-gpu-data",
              "queue_limit": 100,
              "throughput": 34.33,
              "accuracy": 0.21,
              "energy_consumption": 163.0,
              "content_types": [
                "node_attribute:bounding_box",
                "node_attribute:label",
                "node_attribute:confidence",
                "node:person",
                "node:car"
              ],
              "queue_size": 0,
              "queue_space": 100,
              "queue_space_percent": 1.0
            },
            "object-detection-ssd-data": {
              "service_type": "ObjectDetection",
              "stream_key": "object-detection-ssd-data",
              "queue_limit": 100,
              "throughput": 45.6,
              "accuracy": 0.21,
              "energy_consumption": 128.0,
              "content_types": [
                "node_attribute:bounding_box",
                "node_attribute:label",
                "node_attribute:confidence",
                "node:person",
                "node:car"
              ],
              "queue_size": 457,
              "queue_space": -357,
              "queue_space_percent": -3.57
            }
          },
          "total_number_workers": 2
        }
      },
      "id": "AdaptationMonitor:17a36df8-87c4-4c03-9bcf-0e2e76339283",
      "tracer": {
        "headers": {
          "uber-trace-id": "522f6a73dcbc933d:5f49448e540b9f3b:73a437d4feebdf34:1"
        }
      }
    },
    "timestamp": 1740330033.123017
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "522f6a73dcbc933d:9bb3ec120af49088:bc325380835595ae:1"
    }
  }
}
```

## UNNECESSARY_LOAD_SHEDDING_REQUESTED
Default stream id: UnnecessaryLoadSheddingPlanRequested
Example:
```json

{
  "id": "AdaptationAnalyser:45897698-f39c-4030-8582-f699d8eda593",
  "change": {
    "type": "UnnecessaryLoadSheddingPlanRequested",
    "cause": {
      "service_workers": {
        "ObjectDetection": {
          "workers": {
            "object-detection-ssd-gpu-data": {
              "service_type": "ObjectDetection",
              "stream_key": "object-detection-ssd-gpu-data",
              "queue_limit": 100,
              "throughput": 34.33,
              "accuracy": 0.21,
              "energy_consumption": 163.0,
              "content_types": [
                "node_attribute:bounding_box",
                "node_attribute:label",
                "node_attribute:confidence",
                "node:person",
                "node:car"
              ],
              "queue_size": 0,
              "queue_space": 100,
              "queue_space_percent": 1.0
            },
            "object-detection-ssd-data": {
              "service_type": "ObjectDetection",
              "stream_key": "object-detection-ssd-data",
              "queue_limit": 100,
              "throughput": 45.6,
              "accuracy": 0.21,
              "energy_consumption": 128.0,
              "content_types": [
                "node_attribute:bounding_box",
                "node_attribute:label",
                "node_attribute:confidence",
                "node:person",
                "node:car"
              ],
              "queue_size": 80,
              "queue_space": 20,
              "queue_space_percent": 0.20
            }
          },
          "total_number_workers": 2
        }
      },
      "id": "AdaptationMonitor:17a36df8-87c4-4c03-9bcf-0e2e76339433",
      "tracer": {
        "headers": {
          "uber-trace-id": "522f6a73dcbc933d:5f49448e540b9f3b:73a437d4feebdf34:2"
        }
      }
    },
    "timestamp": 1740330033.123017
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "522f6a73dcbc933d:9bb3ec120af49088:bc325380835595ae:2"
    }
  }
}
```

## SERVICE_WORKER_SLR_PROFILE_PLANNED
Default stream id: ServiceWorkerSLRProfilePlanned
Example:
```json
{
  "id": "AdaptationPlanner:ae1fe367-66ab-4f9c-8cf4-90156e994184",
  "plan": {
    "type": "ServiceWorkerSLRProfilePlanned",
    "execution_plan": {
      "strategy": {
        "name": "QQoS-TK-LP",
        "dataflows": {
          "ecc611480b5ba2c41d3b49cb8b36600e": [
            [
              null,
              [
                [
                  "object-detection-ssd-gpu-data"
                ],
                [
                  "wm-data"
                ]
              ]
            ]
          ]
        }
      }
    },
    "change_request": {
      "type": "ServiceWorkerSLRProfileChangePlanRequested",
      "cause": {
        "id": "SLRWorkerRanking:033e4845-923f-4dfc-96cd-9b7ff018a100",
        "service_type": "ObjectDetection",
        "slr_profiles": {
          "ObjectDetection-[0.7, 0.9, 1.0]-[0.5, 0.7, 0.9]-[0.3, 0.5, 0.7]": {
            "query_ids": [
              "a04e8f33c7a272477e0e6779afd84a5b"
            ],
            "criteria_weights": [
              [
                0.7,
                0.9,
                1.0
              ],
              [
                0.5,
                0.7,
                0.9
              ],
              [
                0.3,
                0.5,
                0.7
              ]
            ],
            "alternatives_ids": [
              "object-detection-ssd-gpu-data"
            ],
            "ranking_index": [
              0
            ],
            "ranking_scores": [
              0
            ]
          }
        },
        "tracer": {
          "headers": {
            "uber-trace-id": "4075e6ac22a8af8a:936b2a63c5c37884:de5058a938f27734:1"
          }
        }
      },
      "timestamp": 1740326086.827682
    }
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:b1bd1580d9898def:a652bbd3c6187a2a:1"
    }
  }
}
```


## NEW_QUERY_SCHEDULING_PLANNED
Default stream id: NewQuerySchedulingPlanned
Example:
```json
{
  "id": "AdaptationPlanner:77998cf2-bb19-4838-92b5-625870cb3039",
  "plan": {
    "type": "NewQuerySchedulingPlanned",
    "execution_plan": {
      "strategy": {
        "name": "QQoS-TK-LP",
        "dataflows": {
          "ecc611480b5ba2c41d3b49cb8b36600e": [
            [
              null,
              [
                [
                  "object-detection-ssd-gpu-data"
                ],
                [
                  "wm-data"
                ]
              ]
            ]
          ]
        }
      }
    },
    "change_request": {
      "type": "NewQuerySchedulingPlanRequested",
      "cause": {
        "subscriber_id": "sub_id",
        "query_id": "69ece7da9c73c2c54750fb0489cf8bf8",
        "parsed_query": {
          "name": "PeopleWithCup",
          "output": [
            "AnnotatedRetVideoStream"
          ],
          "from": [
            "publisher1"
          ],
          "content": [
            "ObjectDetection"
          ],
          "match": "MATCH (p:person)-[:same_frame]-(c:cup)",
          "optional_match": "",
          "where": "",
          "window": {
            "window_type": "TUMBLING_COUNT_WINDOW",
            "args": [
              10
            ]
          },
          "ret": "RETURN p, c",
          "qos_policies": {
            "accuracy": "medium_importance",
            "latency": "medium_high_importance",
            "energy_consumption": "high_importance"
          }
        },
        "query_received_event_id": "AccessPoint:61316eac-39d6-4412-a2fa-06f3df72edb7",
        "buffer_stream": {
          "publisher_id": "publisher1",
          "buffer_stream_key": "ecc611480b5ba2c41d3b49cb8b36600e",
          "source": "rtmp://172.17.0.1:1934/live/mystream",
          "resolution": "720x480",
          "fps": "15"
        },
        "service_chain": [
          "ObjectDetection"
        ],
        "id": "ClientManager:5e2d2c08-db56-4d08-86b2-f6e9ad614658",
        "tracer": {
          "headers": {
            "uber-trace-id": "a5eb5fe4cba87746:c161b84f04a6782f:faf7d1291e28ec2f:1"
          }
        }
      },
      "timestamp": 1740330093.163646
    }
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "a5eb5fe4cba87746:41ad3a1e59e8487a:a51173cbbf34fead:1"
    }
  }
}
```


## SERVICE_WORKER_OVERLOADED_PLANNED
Default stream id: ServiceWorkerOverloadedPlanned
Example:
```json
{
  "id": "AdaptationPlanner:0827f4e8-5c66-47db-b329-3499bd26f6cb",
  "plan": {
    "type": "ServiceWorkerOverloadedPlanned",
    "execution_plan": {
      "strategy": {
        "name": "QQoS-TK-LP",
        "dataflows": {
          "ecc611480b5ba2c41d3b49cb8b36600e": [
            [
              null,
              [
                [
                  "object-detection-ssd-gpu-data"
                ],
                [
                  "wm-data"
                ]
              ]
            ]
          ]
        }
      }
    },
    "change_request": {
      "type": "ServiceWorkerOverloadedPlanRequested",
      "cause": {
        "service_workers": {
          "ObjectDetection": {
            "workers": {
              "object-detection-ssd-gpu-data": {
                "service_type": "ObjectDetection",
                "stream_key": "object-detection-ssd-gpu-data",
                "queue_limit": 100,
                "throughput": 34.33,
                "accuracy": 0.21,
                "energy_consumption": 163.0,
                "content_types": [
                  "node_attribute:bounding_box",
                  "node_attribute:label",
                  "node_attribute:confidence",
                  "node:person",
                  "node:car"
                ],
                "queue_size": 0,
                "queue_space": 100,
                "queue_space_percent": 1.0
              },
              "object-detection-ssd-data": {
                "service_type": "ObjectDetection",
                "stream_key": "object-detection-ssd-data",
                "queue_limit": 100,
                "throughput": 45.6,
                "accuracy": 0.21,
                "energy_consumption": 128.0,
                "content_types": [
                  "node_attribute:bounding_box",
                  "node_attribute:label",
                  "node_attribute:confidence",
                  "node:person",
                  "node:car"
                ],
                "queue_size": 457,
                "queue_space": -357,
                "queue_space_percent": -3.57
              }
            },
            "total_number_workers": 2
          }
        },
        "id": "AdaptationMonitor:dff6c999-29a0-41ce-b8fb-d91514f1b5a9",
        "tracer": {
          "headers": {
            "uber-trace-id": "fafa57db908a116f:9263923b8edaec70:aa4514d7f9971e63:1"
          }
        }
      },
      "timestamp": 1740330056.17268
    }
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "fafa57db908a116f:66973e1fb6b77052:6ca4b231f6a1264d:1"
    }
  }
}
```


## SERVICE_WORKER_BEST_IDLE_PLANNED
Default stream id: ServiceWorkerBestIdlePlanned
Example:
```json
{
  "id": "AdaptationPlanner:2a04cba8-e39e-4c02-9405-df472b240018",
  "plan": {
    "type": "ServiceWorkerBestIdlePlanned",
    "execution_plan": {
      "strategy": {
        "name": "QQoS-TK-LP",
        "dataflows": {
          "ecc611480b5ba2c41d3b49cb8b36600e": [
            [
              null,
              [
                [
                  "object-detection-ssd-gpu-data"
                ],
                [
                  "wm-data"
                ]
              ]
            ]
          ]
        }
      }
    },
    "change_request": {
      "type": "ServiceWorkerBestIdlePlanRequested",
      "cause": {
        "service_workers": {
          "ObjectDetection": {
            "workers": {
              "object-detection-ssd-gpu-data": {
                "service_type": "ObjectDetection",
                "stream_key": "object-detection-ssd-gpu-data",
                "queue_limit": 100,
                "throughput": 34.33,
                "accuracy": 0.21,
                "energy_consumption": 163.0,
                "content_types": [
                  "node_attribute:bounding_box",
                  "node_attribute:label",
                  "node_attribute:confidence",
                  "node:person",
                  "node:car"
                ],
                "queue_size": 0,
                "queue_space": 100,
                "queue_space_percent": 1.0
              },
              "object-detection-ssd-data": {
                "service_type": "ObjectDetection",
                "stream_key": "object-detection-ssd-data",
                "queue_limit": 100,
                "throughput": 45.6,
                "accuracy": 0.21,
                "energy_consumption": 128.0,
                "content_types": [
                  "node_attribute:bounding_box",
                  "node_attribute:label",
                  "node_attribute:confidence",
                  "node:person",
                  "node:car"
                ],
                "queue_size": 90,
                "queue_space": 10,
                "queue_space_percent": 0.10
              }
            },
            "total_number_workers": 2
          }
        },
        "id": "AdaptationMonitor:88a8c4af-2a61-4b0d-a402-94f80fc82180",
        "tracer": {
          "headers": {
            "uber-trace-id": "e144b44940ff66c6:de32184ff23f7c2c:6478a1526485e2c5:1"
          }
        }
      },
      "timestamp": 1740330018.090938
    }
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "e144b44940ff66c6:7d76882d17c76b2:339dc3ce3c143e72:1"
    }
  }
}
```


## UNNECESSARY_LOAD_SHEDDING_PLANNED
Default stream id: UnnecessaryLoadSheddingPlanned
Example:
```json
{
  "id": "AdaptationPlanner:0827f4e8-5c66-47db-b329-3499bd26f6cb",
  "plan": {
    "type": "UnnecessaryLoadSheddingPlanned",
    "execution_plan": {
      "strategy": {
        "name": "QQoS-TK-LP",
        "dataflows": {
          "ecc611480b5ba2c41d3b49cb8b36600e": [
            [
              null,
              [
                [
                  "object-detection-ssd-gpu-data"
                ],
                [
                  "wm-data"
                ]
              ]
            ]
          ]
        }
      }
    },
    "change_request": {
      "type": "UnnecessaryLoadSheddingPlanRequested",
      "cause": {
        "service_workers": {
          "ObjectDetection": {
            "workers": {
              "object-detection-ssd-gpu-data": {
                "service_type": "ObjectDetection",
                "stream_key": "object-detection-ssd-gpu-data",
                "queue_limit": 100,
                "throughput": 34.33,
                "accuracy": 0.21,
                "energy_consumption": 163.0,
                "content_types": [
                  "node_attribute:bounding_box",
                  "node_attribute:label",
                  "node_attribute:confidence",
                  "node:person",
                  "node:car"
                ],
                "queue_size": 0,
                "queue_space": 100,
                "queue_space_percent": 1.0
              },
              "object-detection-ssd-data": {
                "service_type": "ObjectDetection",
                "stream_key": "object-detection-ssd-data",
                "queue_limit": 100,
                "throughput": 45.6,
                "accuracy": 0.21,
                "energy_consumption": 128.0,
                "content_types": [
                  "node_attribute:bounding_box",
                  "node_attribute:label",
                  "node_attribute:confidence",
                  "node:person",
                  "node:car"
                ],
                "queue_size": 80,
                "queue_space": 20,
                "queue_space_percent": 0.20
              }
            },
            "total_number_workers": 2
          }
        },
        "id": "AdaptationMonitor:17a36df8-87c4-4c03-9bcf-0e2e76339433",
        "tracer": {
          "headers": {
            "uber-trace-id": "522f6a73dcbc933d:5f49448e540b9f3b:73a437d4feebdf34:2"
          }
        }
      },
      "timestamp": 1740330033.123017
    }
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "fafa57db908a116f:66973e1fb6b77052:6ca4b231f6a1264d:1"
    }
  }
}
```

## SCHEDULING_PLAN_EXECUTED
Default stream id: SchedulingPlanExecuted
Example:
```json
{
  "id": "Scheduler:bc6b34de-694a-4140-8337-8e9442d30db4",
  "plan": {
    "type": "ServiceWorkerSLRProfilePlanned",
    "execution_plan": {
      "strategy": {
        "name": "QQoS-TK-LP",
        "dataflows": {
          "ecc611480b5ba2c41d3b49cb8b36600e": [
            [
              null,
              [
                [
                  "object-detection-ssd-gpu-data"
                ],
                [
                  "wm-data"
                ]
              ]
            ]
          ]
        }
      }
    },
    "change_request": {
      "type": "ServiceWorkerSLRProfileChangePlanRequested",
      "cause": {
        "id": "SLRWorkerRanking:033e4845-923f-4dfc-96cd-9b7ff018a100",
        "service_type": "ObjectDetection",
        "slr_profiles": {
          "ObjectDetection-[0.7, 0.9, 1.0]-[0.5, 0.7, 0.9]-[0.3, 0.5, 0.7]": {
            "query_ids": [
              "a04e8f33c7a272477e0e6779afd84a5b"
            ],
            "criteria_weights": [
              [
                0.7,
                0.9,
                1.0
              ],
              [
                0.5,
                0.7,
                0.9
              ],
              [
                0.3,
                0.5,
                0.7
              ]
            ],
            "alternatives_ids": [
              "object-detection-ssd-gpu-data"
            ],
            "ranking_index": [
              0
            ],
            "ranking_scores": [
              0
            ]
          }
        },
        "tracer": {
          "headers": {
            "uber-trace-id": "4075e6ac22a8af8a:936b2a63c5c37884:de5058a938f27734:1"
          }
        }
      },
      "timestamp": 1740326086.827682
    }
  },
  "tracer": {
    "headers": {
      "uber-trace-id": "4075e6ac22a8af8a:6b5faffeff5e3620:b1894532896b4f43:1"
    }
  }
}
```

