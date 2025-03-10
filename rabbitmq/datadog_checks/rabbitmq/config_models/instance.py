# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

# This file is autogenerated.
# To change this file you should edit assets/configuration/spec.yaml and then run the following commands:
#     ddev -x validate config -s <INTEGRATION_NAME>
#     ddev -x validate models -s <INTEGRATION_NAME>

from __future__ import annotations

from typing import Any, Mapping, Optional, Sequence, Union

from pydantic import BaseModel, Extra, Field, root_validator, validator

from datadog_checks.base.utils.functions import identity
from datadog_checks.base.utils.models import validation

from . import defaults, validators


class AuthToken(BaseModel):
    class Config:
        allow_mutation = False

    reader: Optional[Mapping[str, Any]]
    writer: Optional[Mapping[str, Any]]


class ExtraMetric(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    name: Optional[str]
    type: Optional[str]


class MetricPatterns(BaseModel):
    class Config:
        allow_mutation = False

    exclude: Optional[Sequence[str]]
    include: Optional[Sequence[str]]


class Metric(BaseModel):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    name: Optional[str]
    type: Optional[str]


class PrometheusPlugin(BaseModel):
    class Config:
        allow_mutation = False

    include_aggregated_endpoint: Optional[bool]
    unaggregated_endpoint: Optional[str]
    url: Optional[str]


class Proxy(BaseModel):
    class Config:
        allow_mutation = False

    http: Optional[str]
    https: Optional[str]
    no_proxy: Optional[Sequence[str]]


class ShareLabel(BaseModel):
    class Config:
        allow_mutation = False

    labels: Optional[Sequence[str]]
    match: Optional[Sequence[str]]


class InstanceConfig(BaseModel):
    class Config:
        allow_mutation = False

    allow_redirects: Optional[bool]
    auth_token: Optional[AuthToken]
    auth_type: Optional[str]
    aws_host: Optional[str]
    aws_region: Optional[str]
    aws_service: Optional[str]
    cache_metric_wildcards: Optional[bool]
    cache_shared_labels: Optional[bool]
    collect_counters_with_distributions: Optional[bool]
    collect_histogram_buckets: Optional[bool]
    collect_node_metrics: Optional[bool]
    connect_timeout: Optional[float]
    disable_generic_tags: Optional[bool]
    empty_default_hostname: Optional[bool]
    enable_health_service_check: Optional[bool]
    exchanges: Optional[Sequence[str]]
    exchanges_regexes: Optional[Sequence[str]]
    exclude_labels: Optional[Sequence[str]]
    exclude_metrics: Optional[Sequence[str]]
    exclude_metrics_by_labels: Optional[Mapping[str, Union[bool, Sequence[str]]]]
    extra_headers: Optional[Mapping[str, Any]]
    extra_metrics: Optional[Sequence[Union[str, Mapping[str, Union[str, ExtraMetric]]]]]
    headers: Optional[Mapping[str, Any]]
    histogram_buckets_as_distributions: Optional[bool]
    hostname_format: Optional[str]
    hostname_label: Optional[str]
    ignore_connection_errors: Optional[bool]
    ignore_tags: Optional[Sequence[str]]
    include_labels: Optional[Sequence[str]]
    kerberos_auth: Optional[str]
    kerberos_cache: Optional[str]
    kerberos_delegate: Optional[bool]
    kerberos_force_initiate: Optional[bool]
    kerberos_hostname: Optional[str]
    kerberos_keytab: Optional[str]
    kerberos_principal: Optional[str]
    log_requests: Optional[bool]
    metric_patterns: Optional[MetricPatterns]
    metrics: Optional[Sequence[Union[str, Mapping[str, Union[str, Metric]]]]]
    min_collection_interval: Optional[float]
    namespace: Optional[str] = Field(None, regex='\\w*')
    nodes: Optional[Sequence[str]]
    nodes_regexes: Optional[Sequence[str]]
    non_cumulative_histogram_buckets: Optional[bool]
    ntlm_domain: Optional[str]
    openmetrics_endpoint: Optional[str]
    password: Optional[str]
    persist_connections: Optional[bool]
    prometheus_plugin: Optional[PrometheusPlugin]
    proxy: Optional[Proxy]
    queues: Optional[Sequence[str]]
    queues_regexes: Optional[Sequence[str]]
    rabbitmq_api_url: Optional[str]
    raw_line_filters: Optional[Sequence[str]]
    raw_metric_prefix: Optional[str]
    read_timeout: Optional[float]
    rename_labels: Optional[Mapping[str, Any]]
    request_size: Optional[float]
    service: Optional[str]
    share_labels: Optional[Mapping[str, Union[bool, ShareLabel]]]
    skip_proxy: Optional[bool]
    tag_by_endpoint: Optional[bool]
    tag_families: Optional[bool]
    tags: Optional[Sequence[str]]
    telemetry: Optional[bool]
    timeout: Optional[float]
    tls_ca_cert: Optional[str]
    tls_cert: Optional[str]
    tls_ignore_warning: Optional[bool]
    tls_private_key: Optional[str]
    tls_protocols_allowed: Optional[Sequence[str]]
    tls_use_host_header: Optional[bool]
    tls_verify: Optional[bool]
    use_latest_spec: Optional[bool]
    use_legacy_auth_encoding: Optional[bool]
    use_process_start_time: Optional[bool]
    username: Optional[str]
    vhosts: Optional[Sequence[str]]

    @root_validator(pre=True)
    def _initial_validation(cls, values):
        return validation.core.initialize_config(getattr(validators, 'initialize_instance', identity)(values))

    @validator('*', pre=True, always=True)
    def _ensure_defaults(cls, v, field):
        if v is not None or field.required:
            return v

        return getattr(defaults, f'instance_{field.name}')(field, v)

    @validator('*')
    def _run_validations(cls, v, field):
        if not v:
            return v

        return getattr(validators, f'instance_{field.name}', identity)(v, field=field)

    @root_validator(pre=False)
    def _final_validation(cls, values):
        return validation.core.finalize_config(getattr(validators, 'finalize_instance', identity)(values))
