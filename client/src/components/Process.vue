<template>
    <v-stepper v-model="e1">
        <v-stepper-header>
        <v-avatar color="indigo" size="48" style="margin:auto">
        <span class="white--text headline">{{process.pk}}</span>
        </v-avatar>
        <p style="margin:auto">{{process.fields.title}}</p>
        <p style="margin:auto">-</p>
        <p style="margin:auto">{{process.fields.status}}</p>
        <v-stepper-step :complete="e1 > 1" step="1">Step 1</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="e1 > 2" step="2">Step 2</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="e1 > 3" step="3">Step 3</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step  step="4">Step 4</v-stepper-step>
        
        <v-icon @click='detailShow=!detailShow'>mdi-chevron-down</v-icon>
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
    }
</script>