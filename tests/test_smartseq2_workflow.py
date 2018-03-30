from hcacn.core import Schedule,Configure
from hcacn.steps import FastqDump
from hcacn.steps import Hisat2
from hcacn.steps import Tophat2
from hcacn.steps import SamToBam
from hcacn.steps import BamSort
from hcacn.steps import Cufflinks
from hcacn.steps import Cuffmerge
from hcacn.steps import Cuffquant
from hcacn.steps import Cuffdiff
from hcacn.steps import FastQC

Configure.setIdentity('sqchen0327')
def smartseq_flow(sraInput, ht2Idx_ref, gtf_ref, fa_ref, threads):
    fastq_dump = FastqDump(sraInput1=sraInput)
    hisat = Hisat2(ht2Idx=ht2Idx_ref)(fastq_dump)
    sam2bam = SamToBam(threads=threads)(hisat)
    bamsort = BamSort()(sam2bam)
    cufflinks = Cufflinks(gtfInput=gtf_ref,threads=threads)(bamsort)
    cuffmerge = Cuffmerge(faInput1=fa_ref,gtfInput1=gtf_ref,threads=threads)(cufflinks)
    cuffquant = Cuffquant(threads=threads)(bamsort,cuffmerge)
    cuffdiff = Cuffdiff(faInput=fa_ref,threads=threads)(cuffmerge,cuffquant)
    Schedule.run()

def smartseq_flow2(sraInput, ht2Idx_ref, gtf_ref, fa_ref, threads):
    fastq_dump = FastqDump(sraInput1=sraInput)
    hisat = Hisat2(ht2Idx=ht2Idx_ref)(fastq_dump)
    sam2bam = SamToBam(threads=threads)(hisat)
    bamsort = BamSort()(sam2bam)
    cufflinks = Cufflinks(gtfInput=gtf_ref,threads=threads)(bamsort)
    cuffmerge = Cuffmerge(faInput1=fa_ref,gtfInput1=gtf_ref,threads=threads)(cufflinks)
    cuffquant = Cuffquant(threads=threads)(bamsort,cuffmerge)
    cuffnorm = Cuffnorm(threads=threads)(cuffquant,cuffmerge)
    Schedule.run()

def smartseq_flow3(sraInput, bt2Idx_ref, gtf_ref, fa_ref, threads):
    fastq_dump = FastqDump(sraInput1=sraInput)
    tophat = Tophat2(bt2Idx=bt2Idx_ref,gtfInput=gtf_ref,threads=threads)(fastq_dump)
    sam2bam = SamToBam(threads=threads)(tophat)
    # bamsort = BamSort()(sam2bam)
    # cufflinks = Cufflinks(gtfInput=gtf_ref,threads=threads)(bamsort)
    # cuffmerge = Cuffmerge(faInput1=fa_ref,gtfInput1=gtf_ref,threads=threads)(cufflinks)
    # cuffquant = Cuffquant(threads=threads)(bamsort,cuffmerge)
    # cuffnorm = Cuffnorm(threads=threads)(cuffquant,cuffmerge)
    Schedule.run()



# smartseq_flow(sraInput='/data8t_1/chenshengquan/minidata/test_sra', 
#     ht2Idx_ref="/data8t_1/ref/smartseq/hg19_index/genome", 
#     gtf_ref='/data8t_1/ref/smartseq/genome.gtf', 
#     fa_ref='/data8t_1/ref/smartseq/hg19.fa', 
#     threads=16)
# smartseq_flow2(sraInput='/data8t_1/chenshengquan/minidata/test_sra', 
#     ht2Idx_ref="/data8t_1/ref/smartseq/hg19_index/genome", 
#     gtf_ref='/data8t_1/ref/smartseq/genome.gtf', 
#     fa_ref='/data8t_1/ref/smartseq/hg19.fa', 
#     threads=16)
smartseq_flow3(sraInput='/data8t_1/chenshengquan/minidata/test_sra', 
    bt2Idx_ref="/data8t_1/ref/smartseq/hg19_bt2_index/bt2_index", 
    gtf_ref='/data8t_1/ref/smartseq/genome.gtf', 
    fa_ref='/data8t_1/ref/smartseq/hg19.fa', 
    threads=16)
