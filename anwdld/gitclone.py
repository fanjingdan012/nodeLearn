import os
from multiprocessing import Process, Pool


def run_clone(p_name):
    command = "git clone ssh://i312177@git.wdf.sap.corp:29418/anywhere/%s.git" % p_name

    print (command)
    #os.system(command)


projects=["access-metrics","alpha","android-core","android-stream","api-docs","api-docs-tool",
"app-googlesheet","app-hub","app-int","app-mgt","attachment","auto-infra","b2b","b2b-adapter","b2b-sales-ui",
"b2c-mono","bff-mobile","bff-web","bo-meta-tool","bss","bss-cloudreport","bss-init","bss-ui","burpci",
"campaign","cd","cd-analysis","cd-doctor","cd-info","cd-mock","cd-monitor","cd-monitor-ui","cd-srv",
"cd-srv-ui","cdn","cdx","change-log","channel-adapter","channel-frw","channel-lcm","charts","clair-scan",
"clairctl","cluster-autoscaler","cmt","cmt-config","cmt-go","cmt-proxy","co-config","conf-bee","confbee-store","",
"contract","crm","cron-service","crs","crs-front","crs-operator","dependency-check","deployer","dev-info",
"devops-dashboard","devportal","dkom-eshop","docportal","ecloud-controller-manager","email","email-tmpl",
"employee","ems","eshop","eshop-adapter","event-monitoring","exception-log-processor","extra-domains",
"fallback","frw","frw-version-check","generic-print","go-cd","goidc","heapster","helm-chart","hit","imap-server",
"idp","identity-server","import-export","influx-load","ingress-proxy","init-data","init-node","integration-b1-anw",
"inventory","ios-common","ios-core","ios-hybrid","ios-stream","k8s-watcher","kafka-log-processor","keycloak",
"kibana","knowledge-base","kubebeat","lean","local-git","meta","meta-infra","meta-migration","metrics-api-server",
"metrics-cronjob","microsite","migration-ta","migration-tool","mobile-meta","mobile-proxy","mobile-proxy-go",
"monitor","monitor-agent","monitoring-conf","monitoring-grafana","mp-adapter","mp-connector","msa-dashboard",
"msa-starter","nginx-accesslog","nginx-lua-prometheus","occ-mono","openapi","ops-tool","pact-broker","pact-compare","passenger",
"payment-intg","perf","perf-benchmark","pipeline","pos-adapter","pos-android","posios","posui","pricing","print-tmpl",
"product","productivity","progress","prt-cmt","rapids","rapids-ci","rapids-ui","raw-log-processor","registry-ext",
"resource-map","resource-monitor","resource-operator","resource-proxy","river","search","security","service-case",
"servicelayer","shipping","signing-authority","sip","smart-parser","sms","socket-web","springboot-demo","static-resource",
"status-page","swagger-synchronizer","ta","ta-flow","ta-hf","ta-report","ta-sanity","tax-engine-proxy","telegraf",
"tenant","tenantcn","test","test-coverage","thinclient","third-party-reg","tsui","udo","ui-app-ana","ui-app-b2c",
"ui-app-crm","ui-app-dch","ui-app-dpp","ui-app-empl","ui-app-ext","ui-app-inventory","ui-app-kb","ui-app-misc",
"ui-app-nav","ui-app-pricing","ui-app-product","ui-app-progress","ui-app-sc","ui-app-sip","ui-app-sms","ui-app-taxengine",
"ui-app-tce","ui-core","ui-demo-gpec","ui-ext-dix","ui-login","ui-utils","ui-utils-i18n","vault","vault-config",
"vault-proxy","vault-ui","watchdog","youzan-sdk","zabbix-agent"]
#
# pool = Pool(8)
for p in projects:
    run_clone(p)
    # pool.apply_async(run_clone, (p,))
# pool.close()
# pool.join()
