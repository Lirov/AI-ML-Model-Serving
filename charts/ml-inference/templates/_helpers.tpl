{{- define "ml-inference.name" -}}
ml-inference
{{- end -}}

{{- define "ml-inference.fullname" -}}
{{- printf "%s-%s" .Release.Name (include "ml-inference.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
