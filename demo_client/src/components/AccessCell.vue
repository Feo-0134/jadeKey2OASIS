<template>
    <el-container>
            {{accessmsg}}
    </el-container>
</template>

<script>
var Msal = require('msal');
export default {
    name: 'AccessCell',
    data() {
        return {
            /* AAD API params */
            msalConfig: {
                auth: {
                    clientId: "c6c7e163-aa0b-4185-b95d-0073ee49fa22", //This is your client ID
                    authority:
                    "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47" //This is your tenant info
                },
                cache: {
                    cacheLocation: "localStorage",
                    storeAuthStateInCookie: true
                }
            },
            graphConfig: {
                graphMeEndpoint: "https://graph.microsoft.com/v1.0/me"
            },
            requestObj: {
                    scopes: ["user.read"]
            },

            /* AAD result */
            noInform: false, // if failed to get data
            accessmsg: '',   // result object 
        }
    },
    mounted() {
        this.acquireTokenPopupAndCallMSGraph();
    },
    computed: {
    },
    methods: {
        

        /* AAD related */
        acquireTokenPopupAndCallMSGraph() {
            var that = this
            // Always start with acquireTokenSilent to obtain a token in the signed in user from cache
            var myMSALObj = new Msal.UserAgentApplication(this.msalConfig);
            // (optional when using redirect methods) register redirect call back for Success or Error
            // myMSALObj.handleRedirectCallback(this.authRedirectCallBack);
            myMSALObj.acquireTokenSilent(this.requestObj)
            .then(function (tokenResponse) {
                that.callMSGraph(that.graphConfig.graphMeEndpoint, tokenResponse.accessToken, that.graphAPICallback);
            })
            .catch(function (error) {
                window.console.log(error);
                //this.addFeedback('error', 'System Error. Please turn to the developer.');
                // Upon acquireTokenSilent failure (due to consent or interaction or login required ONLY)
                // Call acquireTokenPopup(popup window)
                if (that.requiresInteraction(error.errorCode)) {
                    myMSALObj.acquireTokenPopup(that.requestObj).then(function (tokenResponse) {
                        that.callMSGraph(that.graphConfig.graphMeEndpoint, tokenResponse.accessToken, that.graphAPICallback);
                    }).catch(function (error) {
                        window.console.log(error);
                        // that.addFeedback('error', 'System Error. Please turn to the developer.');
                    });
                }
            });
        },
        
        // callback for using redirect methods
        authRedirectCallBack(error, response) {
            if (error) {
                window.console.log(error);
                //this.addFeedback('error', 'System Error. Please turn to the developer.');
            } else {
                if (response.tokenType === "access_token") {
                    this.callMSGraph(this.graphConfig.graphMeEndpoint, response.accessToken, this.graphAPICallback);
                } else {
                    window.console.log("token type is:" + response.tokenType);
                }
            }
        },

        // a savage for request AAD resource
        callMSGraph(theUrl, accessToken, callback) {
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.onreadystatechange = function() {
                if (this.readyState == 4 && this.status == 200)
                callback(JSON.parse(this.responseText));
            };
            xmlHttp.open("GET", theUrl, true); // true for asynchronous
            xmlHttp.setRequestHeader("Authorization", "Bearer " + accessToken);
            xmlHttp.send();
        },

        // process AAD result
        graphAPICallback(data) {
            window.console.log("graphAPICallback");
            let result = JSON.stringify(data, null, 4);
            let jsonresult = JSON.parse(result);
            this.accessmsg = jsonresult
        },

        requiresInteraction(errorCode) {
            if (!errorCode || !errorCode.length) {
                return false;
            }
            return errorCode === "consent_required" ||
                errorCode === "interaction_required" ||
                errorCode === "login_required";
        },
    }
}
</script>
