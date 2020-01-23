<template>
    <v-container>
        <v-card max-width="344" class="mx-auto">
            <v-list-item>

            <v-list-item-content>
                <v-list-item-title class="headline mt-3">{{ fullName }}</v-list-item-title>
                <v-list-item-subtitle >{{ alias }}</v-list-item-subtitle>

            </v-list-item-content>
            <v-list-item-avatar color="red" size="60">
                    <span class="white--text mp-2">{{ shortName }}</span>
            </v-list-item-avatar>
            </v-list-item>
            <v-card-text>
            {{ engineer_info }}<br>
            
            {{ engineer_title }}
            </v-card-text>
            <v-card-text>
            Current Process: {{ process_kind }}<br>
            Current Stage: {{ stage_kind }}<br>
            </v-card-text>

            <v-card-actions>
            <v-btn @click="detailShow = !detailShow" class="ml-2" text>
            DETAIL
            <v-icon class="ml-2">mdi-page-next-outline</v-icon>
            </v-btn>
            <v-btn
                text
                @click="showProcessDetail"
                class="ml-2"
                v-if="process_kind && stage_kind"
            >
                EDIT
                <v-icon class="ml-2">mdi-lead-pencil</v-icon>
            </v-btn>
            <v-btn
                v-if="(!(process_kind && stage_kind) )&&engineer_info.id === $store.state.id"
                text
                @click="newProcess"
                class="ml-1"
            >
                START
                <v-icon class="ml-2">mdi-plus-circle-outline</v-icon>
            </v-btn>
            </v-card-actions>
                        <v-stepper v-show='detailShow' v-model="currentStage">
                <div class="ma-3">{{ process_Title }} Proces Detail</div>
                <v-stepper-header>
                    <v-stepper-step :complete="currentStage > 1" step="1"></v-stepper-step>

                    <v-divider></v-divider>

                    <v-stepper-step :complete="currentStage > 2" step="2"></v-stepper-step>

                    <v-divider></v-divider>

                    <v-stepper-step :complete="currentStage > 3" step="3"></v-stepper-step>
                                        
                    <v-divider></v-divider>

                    <v-stepper-step step="4"></v-stepper-step>
                </v-stepper-header>

                <v-stepper-items>
                <v-stepper-content step="1">
                    <v-card
                    class="mb-4"
                    color="red lighten-2"
                    height="220px"
                    >
                    <v-carousel
                        
                        height="200"
                        hide-delimiter-background
                        show-arrows-on-hover
                    >
                        <v-carousel-item
                        v-for="(comment, i) in comment_list"
                        v-show="comment.Stage == currentStage"
                        :key="i"
                        >
                        <v-sheet
                            :color="colors[i]"
                            height="100%"
                            
                        >
                            <v-row
                            class="fill-height"
                            align="center"
                            justify="center"
                            >
                            <div class="display-1">{{ comment.Context }}</div>
                            </v-row>
                        </v-sheet>
                        </v-carousel-item>
                    </v-carousel>
                    </v-card>

                    <v-btn
                    color="primary"
                    @click="processGoOn()"
                    >
                    Continue
                    </v-btn>

                    
                </v-stepper-content>

                <v-stepper-content step="2">
                    <v-card
                    class="mb-4"
                    color="red lighten-2"
                    height="220px"
                    >
                        <v-carousel
                            
                            height="200"
                            hide-delimiter-background
                            show-arrows-on-hover
                        >
                            <v-carousel-item
                            v-for="(comment, i) in comment_list"
                            :key="i"
                            v-show="comment.Stage == currentStage"
                            >
                            <v-sheet
                                :color="colors[i]"
                                height="100%"
                            >
                                <v-row
                                class="fill-height"
                                align="center"
                                justify="center"
                                >
                                <div class="display-1">{{ comment.Context }}</div>
                                </v-row>
                            </v-sheet>
                            </v-carousel-item>
                        </v-carousel>
                    </v-card>
                    <v-btn
                    color="primary"
                    @click="processGoOn()"
                    >
                    Continue
                    </v-btn>

                    
                </v-stepper-content>

                <v-stepper-content step="3">
                    <v-card
                    class="mb-4"
                    color="grey lighten-1"
                    height="200px"
                    ></v-card>

                    <v-btn
                    color="primary"
                    @click="processGoOn()"
                    >
                    Continue
                    </v-btn>

                    
                </v-stepper-content>
                <v-stepper-content step="4">
                    <v-card
                    class="mb-4"
                    color="grey lighten-1"
                    height="200px"
                    ></v-card>

                    <v-btn
                    color="primary"
                    @click="processGoOn()"
                    >
                    Continue
                    </v-btn>

                    
                </v-stepper-content>
                </v-stepper-items>
            </v-stepper>
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
        currentStage: 0,
        maxCurrentStage: 0,
        engineer_title: null,
        process_kind: null,
        stage_kind: null,
        colors: [
          'indigo',
          'warning',
          'pink darken-2',
          'red lighten-1',
          'deep-purple accent-4',
        ],
        detailShow: false,
    }),
    asyncComputed: {
        engineer_title_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://localhost:8000/escBackend/engineer_title/`)
                    this.engineer_title = res.data[this.engineer_info.Title - 1].FullName
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        process_kind_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://localhost:8000/escBackend/process_kind/`)
                    this.process_kind = res.data[this.engineer_info.Title - 1].FullName
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        stage_kind_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://localhost:8000/escBackend/stage_kind/`)
                    this.currentStage = this.engineer_info.EngineerLatestStage
                    this.maxCurrentStage = this.engineer_info.EngineerLatestStage
                    this.stage_kind = res.data[this.engineer_info.EngineerLatestStage - 1].FullName
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            },
            watch: ['engineer_info']
        },
        process_object: {
            async get() {
                try {
                    const path = 'http://localhost:8000/escBackend/process/' + this.engineer_info.EngineerLatestProcess + '/'
                    const res = await this.$http.get(path)
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        comment_list: {
            async get(){
                try {
                    let that = this
                    let commentArray = []
                    // window.console.log(this.process_object.ProcessComments)
                    for (let n=0;n<this.process_object.ProcessComments.length;n++) {
                        const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/comment/${that.process_object.ProcessComments[n]}`)
                        commentArray.push(res.data)
                    }
                    // window.console.log(commentArray)
                    return commentArray
                }catch(e) {
                    window.console.log(e)
                }
            }
        },        
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
        },
        process_id: function() {
            return this.engineer_info.EngineerLatestProcess
        }
    },
    methods: {
        showProcessDetail () {
            const newPath = '/processDetail/' + this.process_id
            this.$router.push(newPath)
        },
        processGoOn() {
            if (this.maxCurrentStage > this.currentStage) {
                this.currentStage += 1
            }
            else this.currentStage = 1
        },
        async newProcess() {
            try {
                    const that = this
                    const res = await this.$http.post(
                    'http://localhost:8000/escBackend/process/',
                        {
                            Kind: that.engineer_info.Title,
                            ProcessOwner: that.engineer_info.id,
                            ProcessCurrentStage: 1,
                            Stage1TryTimes: 1,
                            Stage2TryTimes: -1,
                            Stage3TryTimes: -1,
                            Stage4TryTimes: -1
                        },
                    );
                    window.console.log(res.data)
                    const path = 'http://localhost:8000/escBackend/engineer/' + that.engineer_info.id + '/'
                    const processID = res.data.id
                    const res1 = await this.$http.put( path,
                        {
                            "Alias": that.engineer_info.Alias,
                            "Name": that.engineer_info.Name,
                            "Title": that.engineer_info.Title,
                            "EngineerLatestProcess": processID,
                            "EngineerLatestStage": 1,
                            "IsReviewer": that.engineer_info.IsReviewer
                        }
                    );
                    // location.reload();
                    const newPath = '/processDetail/' + res.data.id
                    setTimeout(() => {
                        this.$router.push(newPath)
                    }, 2000);
                    return res1.data
            }catch(e) {
                window.console.log(e);
            }
        }
    }

}
</script>