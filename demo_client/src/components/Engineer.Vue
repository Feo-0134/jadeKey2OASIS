<template>
    <v-container>
        <v-card max-width="344" class="mx-auto">
            <v-list-item>
            <v-list-item-avatar color="red">
                    <span class="white--text MD mp-2">{{ shortName }}</span>
            </v-list-item-avatar>
            <v-list-item-content>
                <v-list-item-title class="headline">{{ fullName }}</v-list-item-title>
                <v-list-item-subtitle >({{ alias }})</v-list-item-subtitle>

            </v-list-item-content>
            <v-btn @click="detailShow = !detailShow" color="#5F6062">
            <v-icon>mdi-unfold-more-horizontal</v-icon>
            </v-btn>
            </v-list-item>
            <v-stepper v-show='detailShow' v-model="e1">
                <div class="ma-3">{{ process_Title }}</div>
                <v-stepper-header>
                    <v-stepper-step :complete="e1 > 1" step="1"></v-stepper-step>

                    <v-divider></v-divider>

                    <v-stepper-step :complete="e1 > 2" step="2"></v-stepper-step>

                    <v-divider></v-divider>

                    <v-stepper-step step="3"></v-stepper-step>
                                        
                    <v-divider></v-divider>

                    <v-stepper-step step="4"></v-stepper-step>
                </v-stepper-header>

                <v-stepper-items>
                <v-stepper-content step="1">
                    <v-card
                    class="mb-4"
                    color="grey lighten-1"
                    height="200px"
                    ></v-card>

                    <v-btn
                    color="primary"
                    @click="e1 = 2"
                    >
                    Continue
                    </v-btn>

                    <v-btn text>Cancel</v-btn>
                </v-stepper-content>

                <v-stepper-content step="2">
                    <v-card
                    class="mb-4"
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
                    class="mb-4"
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

            <v-card-text>
            {{ engineer_info }}
            <v-breadcrumbs :items="items" divider="-"></v-breadcrumbs>
            </v-card-text>

            <v-card-actions>
            <v-btn
                text
                color="blue accent-4"
            >
                Bookmark
            </v-btn>
            <v-btn
                text
                color="blue accent-4"
            >
                Show More
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn icon>
                <v-icon>mdi-heart</v-icon>
            </v-btn>
            <v-btn icon>
                <v-icon>mdi-share-variant</v-icon>
            </v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>
<script>
export default {
    props: {
        engineer_info: Object
    },
    components: {},
    data: () => ({
        e1: 0,
        items: [
                {
                text: 'Submit Request',
                disabled: false,
                href: 'breadcrumbs_dashboard',
                },
                {
                text: 'Checklist Review',
                disabled: false,
                href: 'breadcrumbs_link_1',
                },
                {
                text: 'Materials Incubation',
                disabled: true,
                href: 'breadcrumbs_link_2',
                },
                {
                text: 'Review Meeting',
                disabled: true,
                href: 'breadcrumbs_link_2',
                },
                {
                text: 'Review Complete',
                disabled: true,
                href: 'breadcrumbs_link_2',
                },
            ],
        detailShow: false,
    }),
    asyncComputed: {
    },
    computed: {
        fullName: function() {
            return this.engineer_info.Name
        },
        shortName: function() {
            let nameArray = []
            nameArray.push(this.engineer_info.Name[0])
            nameArray.push(this.engineer_info.Name[1].toUpperCase())
            return nameArray[0][0] + nameArray[1][0]
        },
        alias: function() {
            return this.engineer_info.Alias
        },
        process_Title: function() {
            if(this.engineer_info.Title == 1) 
                return 'SEE Escalation' 
            return  'EE Escalation'
        }
    },
    methods: {

    }

}
</script>