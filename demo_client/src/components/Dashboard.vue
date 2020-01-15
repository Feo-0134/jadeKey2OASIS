<template>
    <v-container>
        <!-- {{engineer_list}} -->
        <v-subheader class="headline">Engineer List</v-subheader>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
        >
            <v-col cols='4'  v-for="n in engineer_list"
            :key="n">
                <Engineer :engineer_info = "n"/>
            </v-col>
        </v-row>
        <v-subheader class="headline">Process List</v-subheader>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
        >
        <v-col cols='4'  v-for="n in process_list"
          :key="n"
          >
          <Process :process_object="n" />
        </v-col>
        </v-row>
        <v-subheader class="headline">Comment List</v-subheader>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
        >
        <v-col cols='4'  v-for="n in comment_list"
          :key="n"
          >
          <Comment :comment_object="n"/>
        </v-col>
        </v-row>
        <v-subheader class="headline">Reviewer List</v-subheader>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
        >
        <v-col cols='4'  v-for="n in reviewer_list"
          :key="n"
          >
          <Engineer :engineer_info = "n"/>
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