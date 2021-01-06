import logging, os, sys, uuid
import requests, argh

def get_script(process_name, filename):
    if process_name == 'bam2fastq':
        sample_name = filename[:-7]
        return f"""
samtools sort -m 4G -n {filename} -o {sample_name}.qsort.bam
bedtools bamtofastq -i {sample_name}.qsort.bam -fq {sample_name}.1.fq -fq2 {sample_name}.2.fq
"""

def submit_job(name, script, mem, work_dir):
    requests.post("http://127.0.0.1:6000/submit", data={
        "name": name,
        "script": script,
        "mem": mem,
        "work_dir": work_dir })
    
def main(process_name, filenames=[]):
    work_dir = os.getcwd()
    for filename in filenames:
        name = str(uuid.uuid4())
        script = get_script(process_name, filename)
        mem = 4
        submit_job(name, script, mem, work_dir)
        print(f"submitted {name}:")
        print(script)

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1], sys.argv[2:])
