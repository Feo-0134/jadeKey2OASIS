<template>
    <v-container>
        <!-- {{engineer_list}} -->
        <v-subheader class="headline">Engineer List</v-subheader>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
        >
            <v-col cols='4'  v-for="(n, i) in engineer_list" v-show="$store.state.role==='reviewer' || $store.state.id===n.id"
            :key="i">
                <Engineer :engineer_info = "n"/>
            </v-col>
        </v-row>
        <v-row v-show="$store.state.role==='admin'">
        <v-subheader class="headline">Reviewer List</v-subheader>
        <v-spacer></v-spacer>
        <v-btn text @click="reviewerShow=!reviewerShow"><v-icon>mdi-chevron-down</v-icon></v-btn>
        </v-row>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
          v-show = "reviewerShow"
        >
        <v-col cols='4'  v-for="(n, i) in reviewer_list" 
          :key="i"
          >
          <Engineer :engineer_info = "n"/>
        </v-col>
        </v-row>
        <v-row v-show="$store.state.role==='admin'">
        <v-subheader class="headline">Process List</v-subheader>
        <v-spacer></v-spacer>
        <v-btn text @click="processShow=!processShow"><v-icon>mdi-chevron-down</v-icon></v-btn>
        </v-row>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
          v-show = "processShow"
        >
        <v-col cols='6'  v-for="(n, i) in process_list"
          :key="i"
          >
          <Process :process_object="n" />
        </v-col>
        </v-row>
        <v-row v-show="$store.state.role==='admin'">
        <v-subheader class="headline">Comment List</v-subheader>
        <v-spacer></v-spacer>
        <v-btn text @click="commentShow=!commentShow"><v-icon>mdi-chevron-down</v-icon></v-btn>
        </v-row>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
          v-show = "commentShow"
        >
        <v-col cols='4'  v-for="(n, i) in comment_list"
          :key="i"
          >
          <Comment :comment_object="n"/>
        </v-col>
        </v-row>
        
    </v-container>
</template>
<script>
import Engineer from '@/components/Engineer.vue';
import Process from '@/components/Process.vue';
import Comment from '@/components/Comment.vue';
export default {
    props: {

    },
    components: { Engineer, Process, Comment },
    data: () => ({
        engineer_cnt: 0,
        process_cnt: 0,
        comment_cnt: 0,
        reviewer_cnt: 0,
        reviewerShow: false,
        processShow: false,
        commentShow: false

    }),
    asyncComputed: {
        engineer_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/engineer/`)
                    this.engineer_cnt = res.data.length
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        process_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/process/`)
                    this.process_cnt = res.data.length
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        },
        comment_list: {
            async get() {
                try {
                    const res = await this.$http.get(`http://127.0.0.1:8000/escBackend/comment/`)
                    this.comment_cnt = res.data.length
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
                    this.reviewer_cnt = res.data.length
                    return res.data
                }catch(e) {
                    window.console.log(e)
                }
            }
        }
    },
    computed: {

    },
    methods: {
        
    }

}
</script>