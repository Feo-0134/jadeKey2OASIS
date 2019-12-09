<template>
    <div>
    <p>{{engineer}}</p>
        <v-toolbar>
            <template v-if="$vuetify.breakpoint.smAndUp">
                <v-avatar color="indigo" size="36" style="margin:auto">
                    <span class="white--text">{{shortName}}</span>
                </v-avatar>
                
            </template>
            <v-toolbar-title>
                <p style="margin:auto">
                    {{process.title}} - {{engineer.name}} - {{process.status}}
                </p>
            </v-toolbar-title>

            <v-spacer></v-spacer>

            <v-toolbar-items>
                <v-btn icon>
                    <v-icon @click='detailShow=!detailShow'>mdi-chevron-down</v-icon>
                </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-stepper v-model="e1">
            <v-stepper-header>
            <v-stepper-step :complete="e1 > 1" step="1">Step 1</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="e1 > 2" step="2">Step 2</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step :complete="e1 > 3" step="3">Step 3</v-stepper-step>

            <v-divider></v-divider>

            <v-stepper-step  step="4">Step 4</v-stepper-step>
            
            
            </v-stepper-header>

            <v-stepper-items v-show="detailShow">
            <v-stepper-content step="1">
                <v-card
                class="mb-12"
                color="grey lighten-1"
                height="200px"
                ></v-card>

                <v-btn color="primary"
                @click="e1 = 2"
                >
                Continue
                </v-btn>

                <v-btn text>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="2">
                <v-card
                class="mb-12"
                color="grey lighten-1"
                height="200px"
                ></v-card>

                <v-btn
                color="primary"
                @click="e1 = 3"
                >
                Continue
                </v-btn>

                <v-btn text>Cancel</v-btn>
            </v-stepper-content>

            <v-stepper-content step="3">
                <v-card
                class="mb-12"
                color="grey lighten-1"
                height="200px"
                ></v-card>

                <v-btn
                color="primary"
                @click="e1 = 4"
                >
                Continue
                </v-btn>

                <v-btn text>Cancel</v-btn>
            </v-stepper-content>
            <v-stepper-content step="4">
                <v-card
                class="mb-12"
                color="grey lighten-1"
                height="200px"
                ></v-card>

                <v-btn
                color="primary"
                @click="e1 = 1"
                >
                Continue
                </v-btn>

                <v-btn text>Cancel</v-btn>
            </v-stepper-content>
            </v-stepper-items>
        </v-stepper>
    </div>
</template>

<script>
    export default {
        props: {
            process: Object,
        },
        data: () => ({
            e1: 1,
            detailShow: false,
        }),
        asyncComputed: {
            engineer: {
                async get() {
                    try {
                        const res = await this.$http.get(`http://127.0.0.1:8000/escapp/engineer/${this.process.engineer}`);
                        // console.log(res)
                        return res.data
                    }catch(e) {
                        // console.log(e);
                    }
                }   
            }
        },
        computed: {
            shortName() {
                var nameArr = this.engineer.name.split(' ')
                return nameArr[0][0] + nameArr[nameArr.length - 1][0]
            }
        }
    }
</script>