import logging, os, sys, uuid
import requests, argh

def get_script(process_name, filename):
    if process_name == 'bam2fastq':
        sample_name = filename[:-7]
        process_name = f"bam2fastq_{sample_name}"
        process_script = f"""
samtools sort -m 4G -n {filename} -o {sample_name}.qsort.bam
bedtools bamtofastq -i {sample_name}.qsort.bam -fq {sample_name}.1.fq -fq2 {sample_name}.2.fq
rm {sample_name}.qsort.bam
"""
        return process_name, process_script

def submit_job(name, script, mem, work_dir):
    data = { "name": name,
             "script": script,
             "mem": mem,
             "work_dir": work_dir }
    ret = requests.post("http://127.0.0.1:6000/submit", json=data)
    print("catgrid said ", ret.text)
    
def main(process_name, filenames=[]):
    work_dir = os.getcwd()
    for filename in filenames:
        name, script = get_script(process_name, filename)
        mem = 4096
        submit_job(name, script, mem, work_dir)
        print(name)
        print(script)
        print(mem)
        print(work_dir)

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1], sys.argv[2:])
