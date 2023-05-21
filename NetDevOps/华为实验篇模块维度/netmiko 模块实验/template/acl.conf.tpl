acl 2000

{% for host in disallow_ip %}
rule deny source {{ host }} 0
{% endfor %}

{% for host in allow_ip %}
rule permit source {{ host }} 0
{% endfor %}

user-interface {{ interface }}

acl 2000 inbound

commit