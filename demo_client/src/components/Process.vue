<template>
    <v-container>
        <v-card>
            <v-app-bar dark color="red">

            <v-toolbar-title>{{process_Owner.Name}} - {{process_title}}</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-dialog v-model="dialog" width="500">
                <template v-slot:activator="{ on }">
                    <v-btn icon v-on="on">
                            <v-icon>mdi-account-edit-outline</v-icon>
                        </v-btn>
                </template>

                <v-card>
                    <v-card-title
                    class="headline red lighten-2"
                    primary-title
                    >
                    Add Reviewer
                    </v-card-title>

                    <v-card class="mx-auto" max-width="400">
                        <v-list
                            :flat="flat"
                            :dense="dense"
                        >
                            <v-list-item-group
                                v-model="model"
                                :multiple="multiple"
                                :mandatory="mandatory"
                                color="indigo"
                            >
                            <v-list-item
                                v-for="(reviewer,i) in reviewer_list"
                                :key="i"
                            >
                                <v-list-item-icon>
                                <v-icon large> mdi-github-box </v-icon>
                                </v-list-item-icon>

                                <v-list-item-content>
                                <v-list-item-title v-text="reviewer.Name"></v-list-item-title>
                                ({{reviewer.Alias}})
                                </v-list-item-content>
                            </v-list-item>
                            </v-list-item-group>
                        </v-list>
                    </v-card>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn color="primary" text @click="setReviewer">
                        Confirm
                    </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            </v-app-bar>

            <v-container>
                {{ process_object }}
            <v-row dense>
                <v-col
                align="center"
                justify="center"
                v-for="(item, i) in items"
                :key="i"
                cols="12"
                >
                <v-card
                    :color="item.color"
                    dark >
                    <div class="d-flex flex-no-wrap justify-space-between">
                    <div>
                        <v-card-title
                        class="headline"
                        v-text="stage_list[i].FullName"
                        >
                        </v-card-title>

                        <v-card-subtitle v-text="item.artist">
                        </v-card-subtitle>            
                    </div>
                        <div class="headline ma-3"
                        size="25"
                        tile>
                        <v-icon>
                            mdi-window-close
                        </v-icon>
                        {{process_tryTimes[i]}}
                        </div>
                    <!-- <v-avatar
                        class="ma-2"
                        size="100"
                        tile
                    >
                        <v-img :src="item.src"></v-img>
                    </v-avatar> -->
                    </div>
                </v-card>
                <v-icon class="my-3" x-large>
                    mdi-timeline-clock-outline
                </v-icon>
                </v-col>
                <v-col cols="12">
                <v-card
                    color="#5F6062"
                    dark
                >
                    <v-card-title class="headline">Review Complete</v-card-title>

                    <v-card-subtitle>More detail about this process.</v-card-subtitle>
                </v-card>
                </v-col>
            </v-row>
            </v-container>
        </v-card>
        
    </v-container>
</template>
<script>
export default {
    props: {
        process_object: Object
    },
    components: {},
    data: () => ({
        stage_cnt: 0,
        dialog: false,
        reviewerID: -1,
        item: {
            icon: 'mdi-wifi',
            text: 'Wifi',
        },
        model: 1,
        multiple: false,
        mandatory: false,
        flat: false,
        dense: false,
        count: 4,
        items: [
            {
            color: '#5F6062',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Submit Request',
            artist: 'Foster the People',
            },
            {
            color: '#8E8989',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Checklist Review',
            artist: 'Ellie Goulding',
            },
            {
            color: '#5F6062',
            src: 'https://cdn.vuetifyjs.com/images/cards/foster.jpg',
            title: 'Submit Request',
            artist: 'Foster the People',
            },
            {
            color: '#8E8989',
            src: 'https://cdn.vuetifyjs.com/images/cards/halcyon.png',
            title: 'Checklist Review',
            artist: 'Ellie Goulding',
            },
        ],
    }),
    asyncComputed: {
        stage_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/stage_kind/`)
                    this.stage_cnt = res.data.length
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        reviewer_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/reviewer/`)
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        process_Owner: {
            async get() {
                try {
                    const that = this
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/engineer/${that.process_object.ProcessOwner}`)
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        }
    },
    computed: {
        process_title: function() {
            return (this.process_object.Kind == 1) ? 'SEE Escalation' : 'EE Escalation'
        },
        process_tryTimes: function() {
            let tryTimesArray = []
            tryTimesArray.push(this.process_object.Stage1TryTimes)
            tryTimesArray.push(this.process_object.Stage2TryTimes)
            tryTimesArray.push(this.process_object.Stage3TryTimes)
            tryTimesArray.push(this.process_object.Stage4TryTimes)
            return tryTimesArray
        }
    },
    methods: {
        async setReviewer() {
            try {
                    const that = this
                    const res = await this.$http.post(
                    'http://localhost:8000/escBackend/process_review/',
                        {
                            Process: that.process_object.id,
                            Reviewer: that.reviewer_list[that.model].id
                        },
                    );
                    // location.reload();
                    // window.console.log(res.data)
                    this.dialog = false
                    return res.data
            }catch(e) {
                window.console.log(e);
            }
        }
    }

}
</script>