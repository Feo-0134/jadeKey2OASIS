<template>
    <div>
        <!-- <p>{{stage_list}}</p>  -->
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
                <v-btn icon @click="showMore()"> 
                    <v-icon >mdi-chevron-down</v-icon>
                </v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <v-stepper v-model="stage">
            <v-stepper-header>
                <v-stepper-step :complete="stage > 1" step="1">Step 1</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :complete="stage > 2" step="2">Step 2</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step :complete="stage > 3" step="3">Step 3</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step  step="4">Step 4</v-stepper-step>
            
            
            </v-stepper-header>

            <v-stepper-items v-show="detailShow == true">
                <v-stepper-content step="1">
                    <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                    >
                    <Comment
                       v-for="(p, index) in comment_list.related_comment" :key="p._id"
                        :pindex="index"
                        :comment_pk="p"
                    > </Comment>
                       <!-- {{comment_list}}-->
                    </v-card>

                    <v-btn color="primary"
                    @click="stage = 2"
                    >
                    Continue
                    </v-btn>

                    <v-btn text @click="showDetailComment()">Edit</v-btn>
                </v-stepper-content>

                <v-stepper-content step="2">
                    <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                    >
                    <Comment
                       v-for="(p, index) in comment_list.related_comment" :key="p._id"
                        :pindex="index"
                        :comment_pk="p"
                    > </Comment>
                       <!-- {{comment_list}}-->
                    </v-card>

                    <v-btn
                    color="primary"
                    @click="stage = 3"
                    >
                    Continue
                    </v-btn>

                    <v-btn text @click="showDetailComment()">Edit</v-btn>
                </v-stepper-content>

                <v-stepper-content step="3">
                    <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                    >
                    <Comment
                       v-for="(p, index) in comment_list.related_comment" :key="p._id"
                        :pindex="index"
                        :comment_pk="p"
                    > </Comment>
                       <!-- {{comment_list}}-->
                    </v-card>

                    <v-btn
                    color="primary"
                    @click="stage = 4"
                    >
                    Continue
                    </v-btn>

                    <v-btn text @click="showDetailComment()">Edit</v-btn>
                </v-stepper-content>
                
                <v-stepper-content step="4">
                    <v-card
                    class="mb-12"
                    color="grey lighten-1"
                    height="200px"
                    >
                    <Comment
                       v-for="(p, index) in comment_list.related_comment" :key="p._id"
                        :pindex="index"
                        :comment_pk="p"
                    > </Comment>
                       <!-- {{comment_list}}-->
                    </v-card>

                    <v-btn
                    color="primary"
                    @click="stage = 1"
                    >
                    Continue
                    </v-btn>

                    <v-btn text @click="showDetailComment()">Edit</v-btn>
                </v-stepper-content>
            </v-stepper-items>
        </v-stepper>
    </div>
</template>

<script>
    import Comment from '@/components/Comment'
    export default {
        props: {
            process: Object,
        },
        components: { Comment },
        data: () => ({
            stage: 1,
            detailShow: false,
            stage_id: null,
            shortName: 'loading ...'
        }),
        asyncComputed: {
            engineer: {
                async get() {
                    try {
                        const res = await this.$http.get(`http://127.0.0.1:8000/assistant/engineer/${this.process.engineer}`);
                        // console.log(res)
                        var nameArr = res.data.name.split(' ')
                        this.shortName = nameArr[0][0] + nameArr[nameArr.length - 1][0]
                        this.stage = parseInt(this.process.status.split('S')[1])
                        return res.data
                    }catch(e) {
                        // console.log(e);
                    }
                }   
            },
            comment_list: {
                async get() {
                try {
                    const res = await this.$http.get(`http://localhost:8000/assistant/stage/${this.process.stage[this.stage-1]}`);
                    return res.data
                }catch(e) {
                    // console.log(e);
                }
                },
                default () {
                    return [{fields:{title: 'undefined'}}] // for typeError: no default value
                }
            }
        },
        computed: {

        },
        methods: {
            showMore() {
                // this.stage_id = (this.stage_list[this.stage - 1]).pk
                this.detailShow = !this.detailShow
            },
            // showDetailComment() {
            //     this.$router.push(`/${this.process.stage[this.stage-1]}/cmt`) 
            // }
        }
    }
</script>