<template>
    <v-container>
        <!-- {{engineer_list}} -->
        <v-subheader class="headline">Engineer List</v-subheader>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
        >
        <v-col cols='4'  v-for="n in engineer_cnt"
          :key="n">
            <Engineer :engineer_id = "n"/>
        </v-col>
        </v-row>
        <v-subheader class="headline">Process List</v-subheader>
        <v-divider></v-divider>
        <v-row
          justify="center"
          align="center"
        >
        <v-col cols='4'  v-for="n in process_cnt"
          :key="n"
          >
          <Process :process_object="process_list[n-1]" />
        </v-col>
        </v-row>
    </v-container>
</template>
<script>
import Engineer from '@/components/Engineer.vue';
import Process from '@/components/Process.vue';
export default {
    props: {

    },
    components: { Engineer, Process },
    data: () => ({
        engineer_cnt: 0,
        process_cnt: 0,
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
        }
    },
    computed: {

    },
    methods: {
        
    }

}
</script>